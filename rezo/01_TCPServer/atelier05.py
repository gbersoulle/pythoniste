import socketserver, time

socketserver.TCPServer.allow_reuse_address = True

HOTE = "127.0.0.1"
PORT = 8808


class ServeurMultiClient(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        ligne = self.rfile.readline().rstrip(b"\n")
        if not ligne:
            return
        print(f"    Reçu de {self.client_address} : {ligne!r}")
        time.sleep(2)  # rend le parallélisme visible
        self.wfile.write(ligne + b"\n")


if __name__ == "__main__":
    with ServeurMultiClient((HOTE, PORT), EchoHandler) as serveur:
        print(f"<<< Serveur multi-clients en attente sur {(HOTE, PORT)}")
        serveur.serve_forever()
