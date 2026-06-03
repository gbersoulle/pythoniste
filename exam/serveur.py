"""Serveur TCP threadé exposant l'annuaire de domaines.

Protocole retenu : Option A — texte ligne (COMMANDE arg\\n)

| Option | Avantages | Inconvénients |
|--------|-----------|---------------|
| A. Texte ligne (SEARCH host\\n) | Lisible, testable avec netcat, simple à parser | Pas binaire-safe |
| B. Préfixe longueur (4 octets BE + payload) | Robuste, binaire-safe | Plus complexe à implémenter |
| C. JSON ligne ({"cmd":"SEARCH","arg":"host"}) | Structuré, validable via Pydantic | Plus verbeux, surcharge pour un usage simple |

Choix justifié : Option A retenue car le client est un script Python interne,
les commandes sont simples et textuelles, et la testabilité avec netcat est un
avantage opérationnel concret sans risque lié au binaire-safe.
"""

import socketserver

from sqlalchemy.exc import IntegrityError

import donnees
from collecte import collecter


class MonServeur(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        ligne = self.rfile.readline().decode().strip()
        if not ligne:
            return
        parties = ligne.split(" ", 1)
        cmd = parties[0].upper()
        arg = parties[1] if len(parties) > 1 else ""

        if cmd == "SEARCH":
            d = donnees.chercher(arg)
            reponse = str(d) if d else "NOT_FOUND"
        elif cmd == "RECORD":
            try:
                domaine = collecter(arg)
                donnees.enregistrer(domaine)
                reponse = "OK"
            except IntegrityError:
                reponse = "ALREADY_EXISTS"
            except Exception as e:
                reponse = f"ERROR {e}"
        elif cmd == "COUNT":
            reponse = str(len(donnees.lister()))
        elif cmd == "LIST":
            reponse = "\n".join(d.hote for d in donnees.lister()) or ""
        else:
            reponse = f"ERROR unknown command {cmd}"

        self.wfile.write((reponse + "\n").encode())


def main(host: str = "0.0.0.0", port: int = 8888) -> None:
    with MonServeur((host, port), Handler) as srv:
        print(f"Serveur démarré sur {host}:{port}")
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print("\nArrêt du serveur.")
