# Mini-annuaire de domaines réseau

Mini-annuaire Python stockant pour chaque hôte : IP résolue, contact whois, email whois.

## Protocole réseau
Option A retenue : les données sont purement textuelles, et la testabilité avec `netcat` est un avantage direct.

## Installation

```bash
sudo apt install whois
pip install -r requirements.txt
```

## Usage

### Démarrer le serveur

```bash
python annuaire.py serve
python annuaire.py serve --host 0.0.0.0 --port 8888
```

### Collecter et enregistrer un domaine

```bash
python annuaire.py record google.com
# OK

python annuaire.py record google.com
# ALREADY_EXISTS
```

### Rechercher un domaine

```bash
python annuaire.py search google.com
# hote='google.com' ip='142.250.74.46' contact=None email=None
```

### Compter les entrées

```bash
python annuaire.py count
# 1
```

### Lister tous les domaines

```bash
python annuaire.py list
# google.com
```

### Verbosité

```bash
python annuaire.py -v search google.com    # INFO
python annuaire.py -vv search google.com   # DEBUG
```

### Test direct avec netcat

```bash
printf -- '%s\n' "COUNT" | nc 127.0.0.1 8888
printf -- '%s\n' "SEARCH google.com" | nc 127.0.0.1 8888
printf -- '%s\n' "LIST" | nc 127.0.0.1 8888
```

