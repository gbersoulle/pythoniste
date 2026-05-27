import socketserver

socketserver.TCPServer.allow_reuse_address = True

HOTE = "127.0.0.1"
PORT = 8808


class EchoHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        ligne = self.rfile.readline().rstrip(b"\n")
        if not ligne:
            return
        print(f"    Reçu de {self.client_address} : {ligne!r}")
        self.wfile.write(ligne + b"\n")


if __name__ == "__main__":
    with socketserver.TCPServer((HOTE, PORT), EchoHandler) as serveur:
        print(f"<<< Echo serveur en attente sur {(HOTE, PORT)}")
        serveur.serve_forever()
