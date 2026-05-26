# Feedback — Atelier 2 (Gaspard BERSOULLE)

## Respect de la consigne

Le script est très concis (8 lignes) :

- les trois sockets demandés dans un `with` imbriqué (continuation
  `\`) ✓
- `fileno()`, `family.name`, `type.name` imprimés ✓ (sur une seule
  ligne par socket, OK)

**Point manquant** : la question sur le `fileno()` n'a pas reçu de
réponse écrite. C'est la moitié pédagogique de l'atelier (le code
sans la réflexion, c'est un demi-rendu). Ajoute un commentaire en
fin de fichier qui explique :

- pourquoi les trois `fileno()` sont nécessairement différents
  (descripteur unique attribué par le noyau, le plus petit entier
  libre de la table) ;
- ce qui se passe à la sortie du `with` (numéro libéré et réutilisable).

## Côté Python (à titre indicatif)

- La forme `for s in (tcp, udp, unix): print(...)` est idiomatique ;
  une variante qui imprime aussi un libellé serait plus lisible :
  ```python
  for nom, s in (("TCP", tcp), ("UDP", udp), ("UNIX", unix)):
      print(f"{nom:5s} fileno={s.fileno()} family={s.family.name} type={s.type.name}")
  ```

---
*Évalué sur le commit `ed41da0` (fichier `atelier02.py`).*
