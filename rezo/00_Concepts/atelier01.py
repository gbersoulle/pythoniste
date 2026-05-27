import sys
import socket

enregistrements = socket.getaddrinfo(sys.argv[1], None)

for famille, *_, (adresse, *__) in enregistrements:
    if famille == socket.AF_INET:
        print(f"IPv4 : {adresse}")
    elif famille == socket.AF_INET6:
        print(f"IPv6 : {adresse}")

print(f"Total : {len(enregistrements)} enregistrement(s)")
