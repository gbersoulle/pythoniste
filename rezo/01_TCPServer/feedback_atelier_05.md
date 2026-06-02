# Feedback — R03/A5 (Serveur TCP multi-clients, BERSOULLE Gaspard)

## Respect de la consigne

Critères attendus : serveur basé sur `socketserver` combinant `ThreadingMixIn` **en premier** et `TCPServer` dans la définition de la classe, avec un `time.sleep` côté handler pour rendre le parallélisme visible.

Constat sur ton code :
- ✓ Ordre d'héritage correct : `class ServeurMultiClient(socketserver.ThreadingMixIn, socketserver.TCPServer)` — le mixin précède bien la classe de base, indispensable pour que la MRO active le comportement multi-threadé.
- ✓ `time.sleep(2)` placé dans `EchoHandler.handle`, juste avant la réponse — permet de vérifier visuellement que deux clients sont servis en parallèle (et pas en file d'attente).
- ✓ `allow_reuse_address = True` positionné en amont, pratique pour relancer le serveur sans attendre le `TIME_WAIT`.
- ✓ Handler basé sur `StreamRequestHandler` avec `rfile`/`wfile` — API plus haut niveau et plus lisible qu'un `BaseRequestHandler` brut.
- ⚠ Le fichier est rangé dans `rezo/01_TCPServer/` au lieu du dossier `rezo/03_Socketserver/` attendu pour R03/A5. Pensé à déplacer pour les prochains rendus afin que les scripts d'évaluation le détectent automatiquement.

---
*Évalué sur le commit `8b18236` (fichier `rezo/01_TCPServer/atelier05.py`).*
