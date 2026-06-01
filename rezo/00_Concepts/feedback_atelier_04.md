# Feedback — R00/A4 (anatomie d'une connexion, BERSOULLE Gaspard)

## Respect de la consigne

Critères attendus : créer une paire avec `socket.socketpair()`, afficher
`fileno()`, `getsockname()` et `getpeername()` sur chaque extrémité,
commenter ce qu'on observe.

Constat sur ton code :

- ✓ `socket.socketpair()` + `with a, b:` pour fermer proprement
- ✓ Boucle `for s in (a, b):` qui imprime `fileno`, `getsockname()` et
  `getpeername()` — symétrique des deux côtés
- ✓ Commentaire pertinent : tu expliques bien que les adresses sont
  vides parce que `socketpair()` crée des sockets AF_UNIX anonymes,
  par opposition à TCP/IPv4 qui aurait IP + port
- ✓ Format `f"...={...!r}"` lisible

Rendu modèle, court et juste.

---
*Évalué sur le commit `66e2045` (fichier `rezo/00_Concepts/atelier04.py`).*
