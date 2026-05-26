# Feedback — Atelier 1 (Gaspard BERSOULLE)

## Respect de la consigne

Le script est très concis (12 lignes) et fait l'essentiel :
argument CLI lu, séparation IPv4 / IPv6, total imprimé.

Trois écarts :

- **Pas de déduplication** : tu parcours `enregistrements` sans
  filtrer les doublons. Comme `getaddrinfo` retourne plusieurs
  tuples par adresse (un par socket type), `google.com` apparaîtra
  plusieurs fois.
- **Total = `len(enregistrements)`** : c'est le nombre brut de
  tuples, pas le nombre d'adresses uniques affichées. Avec dédup,
  il faudrait `len(ipv4) + len(ipv6)`.
- **Affichage entremêlé** : tu imprimes au fur et à mesure dans la
  boucle, donc l'ordre suit ce que retourne `getaddrinfo` (en
  pratique : tous les IPv4 puis tous les IPv6, mais ce n'est pas
  garanti). La consigne attend les IPv4 puis les IPv6 — l'idiome
  est : on collecte d'abord, on affiche ensuite.

## Côté réseau

- Le dépaquetage `for famille, *_, (adresse, *__) in
  enregistrements:` est très astucieux : tu jettes les champs
  intermédiaires et tu dépaquettes le `sockaddr` en sortie. Joli.
- Pour dédupliquer sans trop alourdir, le set est ton ami :
  ```python
  ipv4, ipv6 = set(), set()
  for famille, *_, (adresse, *__) in enregistrements:
      if famille == socket.AF_INET: ipv4.add(adresse)
      elif famille == socket.AF_INET6: ipv6.add(adresse)
  ```
  Puis deux boucles d'affichage.

## Côté Python (à titre indicatif)

- Pas de fonction `main()` ni de garde — pas grave sur 12 lignes.
- Pas de gestion de `socket.gaierror` ni de validation
  `len(sys.argv)` : un domaine inexistant ou un appel sans argument
  fera planter le script.
- Code idiomatique et très compact. Pour la robustesse, ajouter
  juste un `try/except socket.gaierror` autour du `getaddrinfo`
  serait suffisant.

---
*Évalué sur le commit `ed41da0` (fichier `atelier01.py`).*
