import socket

a, b = socket.socketpair()
with a, b:
    for s in (a, b):
        print(f"fileno={s.fileno()}, local={s.getsockname()!r}, pair={s.getpeername()!r}")

# Les adresses sont vides ('') car socketpair() crée des sockets AF_UNIX anonymes : elles ne sont pas bindées à un chemin dans le système de fichiers, contrairement à un socket TCP/IPv4 qui aurait une adresse IP + port.
