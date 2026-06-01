# Feedback — R00/A5 (recv_ligne à la main, BERSOULLE Gaspard)

## Respect de la consigne

Critères attendus : implémenter `recv_ligne(sock) -> bytes` en bouclant
sur `recv(1)` jusqu'à rencontrer `\n`, accumuler les octets, retourner
le contenu sans le saut de ligne.

Constat sur ton code :

- ✓ Boucle `while True` avec `sock.recv(1)`, arrêt sur `b"\n"`
- ✓ Accumulation dans une liste `morceaux` puis `b"".join(...)` —
  idiome Python correct (pas de concaténation `+=` O(n²))
- ✓ Le `\n` n'est pas inclus dans la valeur retournée
- ✓ Commentaire honnête : « Inefficace car un appel système par octet »
  — c'est exactement la leçon de l'atelier, montrer le coût pour
  motiver le préfixe de longueur en A6
- ✓ Démonstration avec deux lignes `b"bonjour\nle monde\n"` consommées
  successivement

Rien à redire.

---
*Évalué sur le commit `66e2045` (fichier `rezo/00_Concepts/atelier05.py`).*
