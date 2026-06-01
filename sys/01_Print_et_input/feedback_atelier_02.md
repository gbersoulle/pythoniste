# Feedback — S01/A2 (prénom + âge, BERSOULLE Gaspard)

## Respect de la consigne

Critères attendus : demander prénom et âge, convertir l'âge en `int`,
calculer l'année de naissance via `date.today().year - age`, gérer le
cas où l'utilisateur saisit autre chose qu'un entier (`ValueError`).

Constat sur ton code :

- ✓ `input("Ton prénom : ")` et `int(input("Ton âge : "))`
- ✓ `from datetime import date` + `date.today().year - age` — c'est
  la bonne primitive (pas `datetime.now().year`, plus lourd)
- ✓ Format de sortie correct, avec `né(e)` neutre en genre
- ⚠ Pas de `try/except ValueError` autour de `int(...)` : si on tape
  « vingt », ça crashe avec un traceback `ValueError`. La consigne
  demandait d'attraper ce cas et d'afficher un message propre (par
  exemple `print("Âge invalide.")` ou `sys.exit(1)`). C'est le seul
  point qui manque.

Pour le reste, le code est minimal et juste.

---
*Évalué sur le commit `` (fichier `sys/01_Print_et_input/atelier_02.py`).*
