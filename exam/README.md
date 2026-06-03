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

python annuaire.py record google.com
# OK
python annuaire.py record google.com
# ALREADY_EXISTS

python annuaire.py search google.com
# hote='google.com' ip='142.250.74.46'

python annuaire.py count
# 1

python annuaire.py list
# google.com

python annuaire.py -v search google.com    # INFO
python annuaire.py -vv search google.com   # DEBUG
```
