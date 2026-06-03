"""Collecte les informations réseau (IP, whois) d'un nom d'hôte."""

import platform
import re
import subprocess

from pydantic import BaseModel, EmailStr


class Domaine(BaseModel):
    hote: str
    ip: str | None
    contact: str | None
    email: EmailStr | None


def resoudre_ip(hote: str) -> str | None:
    systeme = platform.system()
    try:
        res = subprocess.run(
            ["nslookup", hote], capture_output=True, text=True, timeout=5.0
        )
        if res.returncode != 0:
            return None
        # Sur Windows, nslookup n'affiche pas "Non-authoritative answer"
        if systeme == "Windows":
            bloc = res.stdout
        else:
            parties = res.stdout.split("Non-authoritative answer")
            bloc = parties[-1] if len(parties) > 1 else res.stdout
        m = re.search(r"Address:\s+(\d+\.\d+\.\d+\.\d+)", bloc)
        return m.group(1) if m else None
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None


def interroger_whois(hote: str) -> tuple[str | None, str | None]:
    try:
        res = subprocess.run(
            ["whois", hote], capture_output=True, text=True, timeout=10
        )
        if res.returncode != 0:
            return None, None
        texte = res.stdout
        m_contact = re.search(r"Registrant Name:\s*(.+)", texte)
        if not m_contact:
            m_contact = re.search(r"Registrant:\s*(.+)", texte)
        contact = m_contact.group(1).strip() if m_contact else None
        m_email = re.search(r"\S+@\S+", texte)
        email = m_email.group(0) if m_email else None
        return contact, email
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return None, None


def collecter(hote: str) -> Domaine:
    ip = resoudre_ip(hote)
    contact, email = interroger_whois(hote)
    return Domaine(hote=hote, ip=ip, contact=contact, email=email)
