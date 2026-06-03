"""Interface en ligne de commande pour l'annuaire de domaines."""

import argparse
import logging
import socket
import sys

import client
import serveur


def _add_client_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8888)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Mini-annuaire de domaines réseau")
    parser.add_argument("-v", action="count", default=0, dest="verbosity")

    sub = parser.add_subparsers(dest="cmd", required=True)

    p_serve = sub.add_parser("serve", help="Démarre le serveur")
    p_serve.add_argument("--host", default="0.0.0.0")
    p_serve.add_argument("--port", type=int, default=8888)

    p_search = sub.add_parser("search", help="Recherche un hôte")
    p_search.add_argument("hote")
    _add_client_args(p_search)

    p_record = sub.add_parser("record", help="Collecte et enregistre un hôte")
    p_record.add_argument("hote")
    _add_client_args(p_record)

    p_count = sub.add_parser("count", help="Nombre d'hôtes enregistrés")
    _add_client_args(p_count)

    p_list = sub.add_parser("list", help="Liste tous les hôtes")
    _add_client_args(p_list)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    niveaux = [logging.WARNING, logging.INFO, logging.DEBUG]
    logging.basicConfig(level=niveaux[min(args.verbosity, 2)])

    try:
        if args.cmd == "serve":
            serveur.main(args.host, args.port)
        elif args.cmd == "search":
            print(client.cmd_search(args.host, args.port, args.hote))
        elif args.cmd == "record":
            print(client.cmd_record(args.host, args.port, args.hote))
        elif args.cmd == "count":
            print(client.cmd_count(args.host, args.port))
        elif args.cmd == "list":
            for hote in client.cmd_list(args.host, args.port):
                print(hote)
    except (ConnectionRefusedError, socket.timeout) as e:
        sys.exit(f"Erreur de connexion à {args.host}:{args.port} — {e}")
