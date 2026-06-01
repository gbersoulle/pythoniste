# Feedback — S03/A1 (calculatrice argparse, BERSOULLE Gaspard)

## Respect de la consigne

Critères attendus : trois arguments positionnels (`a: float`,
`op: choices=["+", "-", "*", "/"]`, `b: float`), gérer la division par
zéro en écrivant sur `stderr` et en sortant avec `exit(1)`.

Constat sur ton code :

- ✓ Trois positionnels avec les bons types : `a` et `b` en `float`,
  `op` avec `choices=["+", "-", "*", "/"]`
- ✓ Garde `if args.op == "/" and args.b == 0:` puis
  `print(..., file=sys.stderr)` et `sys.exit(1)` — pattern exact
  attendu pour ZeroDivisionError
- ✓ Affichage `f"{a} {op} {b} = {res}"`
- ⚠ Détail : le `dict` `ops` calcule les quatre opérations même si
  une seule sera utilisée — `args.a / args.b` est évalué quoi qu'il
  arrive, mais la garde précédente l'a protégé. Pas un bug, juste un
  peu de calcul inutile. Variante plus standard : `match args.op`
  ou un `if/elif` qui n'évalue que la bonne branche. Aucun impact
  sur la note.

Très bon rendu.

---
*Évalué sur le commit `` (fichier `sys/03_Argparse/atelier_01.py`).*
