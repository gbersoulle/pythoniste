import socket
import struct


def recv_exactement(sock, n: int) -> bytes:
    morceaux = []
    while n > 0:
        morceau = sock.recv(n)
        morceaux.append(morceau)
        n -= len(morceau)
    return b"".join(morceaux)


def envoyer_message(sock, message: bytes) -> None:
    sock.sendall(struct.pack("!I", len(message)) + message)


def recevoir_message(sock) -> bytes:
    longueur = struct.unpack("!I", recv_exactement(sock, 4))[0]
    return recv_exactement(sock, longueur)


messages = [b"a", b"bb", b"ccc"]

a, b = socket.socketpair()
with a, b:
    for msg in messages:
        envoyer_message(a, msg)
    for msg in messages:
        recu = recevoir_message(b)
        assert recu == msg
        print(recu)
