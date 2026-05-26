import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument("--protocole", choices=["tcp", "udp"], required=True)
args = parser.parse_args()

if args.protocole == "tcp":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect(("127.0.0.1", 1))
        except ConnectionRefusedError:
            print("connexion refusée")
else:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(1)
        octets = s.sendto(b"ping", ("127.0.0.1", 1))
        print(f"datagramme envoyé ({octets} octet(s)), aucune confirmation possible")
