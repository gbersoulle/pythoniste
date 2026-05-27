# Feedback — Atelier 3 (Gaspard BERSOULLE)

## Respect de la consigne

Très bien, sur 20 lignes :

- argparse avec `--protocole tcp|udp` requis ✓
- TCP : `with` + `settimeout(1)` + `connect` + `ConnectionRefusedError`
  → message conforme (« connexion refusée ») ✓
- UDP : `sendto` retourne `octets` (typé) → message conforme
  avec le nombre d'octets envoyés ✓

Le code est propre, l'intention claire. C'est un rendu modèle
sans sur-ingénierie.

## Côté Python (à titre indicatif)

- L'usage de `else:` au lieu de `elif args.protocole == "udp":`
  fonctionne parce qu'argparse limite déjà aux deux valeurs via
  `choices` — donc le défaut sera forcément UDP. Pratique courte
  et correcte. Le corrigé utilise aussi cette forme.
- Pas de fonction `main()` ni de garde — pas grave ici.

---
*Évalué sur le commit `4bc5905` (fichier `00_Concepts/atelier03.py`).*
