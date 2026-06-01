# Feedback — R00/A7 (endianness, BERSOULLE Gaspard)

## Respect de la consigne

Critères attendus : sur les 4 octets `b"\x00\x00\x00\x2A"`, faire trois
lectures (`!I`, `<I`, et `!I` sur les octets inversés) et montrer que
« lire en little-endian » équivaut à « inverser puis lire en big-endian ».

Constat sur ton code :

- ✓ Les trois lectures sont là : `!I` (big = 42), `<I` (little =
  704643072), `!I` sur `octets[::-1]` (= 704643072)
- ✓ Commentaire pédagogique au bon endroit qui formule l'équivalence
- ✓ `assert little_endian == inverse_big_endian` valide la démonstration
- ✓ Affichage aligné avec `f"..."` lisible

Rendu modèle, va droit au but.

---
*Évalué sur le commit `66e2045` (fichier `rezo/00_Concepts/atelier07.py`).*
