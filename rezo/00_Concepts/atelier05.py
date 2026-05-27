import socket


def recv_ligne(sock) -> bytes:
    morceaux = []
    while True:
        octet = sock.recv(1) # Inefficace car un appel système par octet
        if octet == b"\n":
            break
        morceaux.append(octet)
    return b"".join(morceaux)


a, b = socket.socketpair()
with a, b:
    a.sendall(b"bonjour\nle monde\n")
    print(recv_ligne(b))
    print(recv_ligne(b))
