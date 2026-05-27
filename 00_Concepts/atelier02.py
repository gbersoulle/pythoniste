import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp, \
     socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp, \
     socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as unix:

    for s in (tcp, udp, unix):
        print(s.fileno(), s.family.name, s.type.name)
