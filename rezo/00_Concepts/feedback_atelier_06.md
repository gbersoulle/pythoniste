# Feedback — R00/A6 (préfixe de longueur, BERSOULLE Gaspard)

## Respect de la consigne

Critères attendus : encadrer chaque message d'un préfixe de longueur
4 octets big-endian (`struct.pack("!I", n)`), envoyer avec `sendall`,
lire exactement N octets côté réception (recv peut renvoyer moins).

Constat sur ton code :

- ✓ `recv_exactement(sock, n)` boucle correctement jusqu'à avoir lu
  les `n` octets — c'est exactement ce qu'on attend pour gérer le
  fait que `recv` peut renvoyer un fragment
- ✓ `envoyer_message` : `sock.sendall(struct.pack("!I", len(msg)) + msg)`
  — `!I` (big-endian, unsigned int 4 octets) et `sendall` (pas `send`)
- ✓ `recevoir_message` : lit 4 octets, décode la longueur, puis lit
  exactement ce nombre d'octets
- ✓ Démonstration avec trois messages de tailles différentes et
  `assert recu == msg` qui valide la sérialisation

Code propre, l'API `envoyer_message` / `recevoir_message` est bien
nommée. Rendu modèle.

---
*Évalué sur le commit `66e2045` (fichier `rezo/00_Concepts/atelier06.py`).*
