"""Client TCP pour l'annuaire de domaines (protocole texte ligne)."""

import socket


def recv_ligne(sock: socket.socket) -> str:
    buf = b""
    while True:
        c = sock.recv(1)
        if not c or c == b"\n":
            break
        buf += c
    return buf.decode().strip()


def recv_all(sock: socket.socket) -> str:
    buf = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        buf += chunk
    return buf.decode()


def cmd_search(host: str, port: int, hote: str) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(10.0)
        s.connect((host, port))
        s.sendall(f"SEARCH {hote}\n".encode())
        return recv_ligne(s)


def cmd_record(host: str, port: int, hote: str) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(10.0)
        s.connect((host, port))
        s.sendall(f"RECORD {hote}\n".encode())
        return recv_ligne(s)


def cmd_count(host: str, port: int) -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(10.0)
        s.connect((host, port))
        s.sendall(b"COUNT\n")
        return int(recv_ligne(s))


def cmd_list(host: str, port: int) -> list[str]:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(10.0)
        s.connect((host, port))
        s.sendall(b"LIST\n")
        data = recv_all(s)
        return [h for h in data.splitlines() if h]
