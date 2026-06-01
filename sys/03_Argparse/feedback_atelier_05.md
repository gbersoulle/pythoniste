# Feedback — S03/A5 (conversion de températures, BERSOULLE Gaspard)

## Respect de la consigne

Critères attendus : `--from` et `--to` (avec `dest=` car `from` est un
mot-clé Python), `choices=["C", "F", "K"]`, conversion par pivot
Celsius (toute échelle → Celsius → toute échelle).

Constat sur ton code :

- ✓ `--from` avec `dest="depuis"` et `--to` avec `dest="vers"` —
  contournement correct du mot-clé `from`
- ✓ Architecture pivot : `vers_celsius(...)` puis `depuis_celsius(...)`
  composées en `depuis_celsius(vers_celsius(v, depuis), vers)` —
  c'est exactement le pattern qui évite la table à 9 cases
- ✓ Formules justes : `(F − 32) × 5/9`, `K − 273.15`, et leurs inverses
- ✓ Bonus `--precision` avec `default=2` et formatage `f"{v:.{prec}f}"`
- ⚠ `choices=echelles` où `echelles = ["celsius", "fahrenheit", "kelvin"]`
  au lieu de `["C", "F", "K"]` demandés dans l'énoncé. La logique est
  identique, mais la CLI est plus verbeuse à l'usage
  (`--from celsius --to fahrenheit` au lieu de `--from C --to F`).
  Détail d'interface, pas de fond.

Rendu très solide, conception propre.

---
*Évalué sur le commit `` (fichier `sys/03_Argparse/atelier_05.py`).*
