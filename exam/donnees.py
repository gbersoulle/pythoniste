"""Persistance des domaines dans une base SQLite via SQLAlchemy."""

from pathlib import Path

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from collecte import Domaine

BDD_PATH = Path(__file__).parent / "domaines.db"


class Base(DeclarativeBase):
    pass


class DomaineDB(Base):
    __tablename__ = "domaines"

    hote = Column(String, primary_key=True)
    ip = Column(String, nullable=True)
    contact = Column(String, nullable=True)
    email = Column(String, nullable=True)


engine = create_engine("sqlite:///" + str(BDD_PATH))
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def enregistrer(domaine: Domaine) -> None:
    session = SessionLocal()
    try:
        session.add(DomaineDB(**domaine.model_dump()))
        session.commit()
    finally:
        session.close()


def lister() -> list[Domaine]:
    session = SessionLocal()
    try:
        resultats = session.query(DomaineDB).all()
        domaines = []
        for d in resultats:
            domaines.append(Domaine(hote=d.hote, ip=d.ip, contact=d.contact, email=d.email))
        return domaines
    finally:
        session.close()


def chercher(hote: str) -> Domaine | None:
    session = SessionLocal()
    try:
        d = session.query(DomaineDB).filter_by(hote=hote).first()
        if d is None:
            return None
        return Domaine(hote=d.hote, ip=d.ip, contact=d.contact, email=d.email)
    finally:
        session.close()
