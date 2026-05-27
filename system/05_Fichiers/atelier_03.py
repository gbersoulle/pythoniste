import argparse, datetime

p = argparse.ArgumentParser()
p.add_argument("message")
args = p.parse_args()

horodatage = datetime.datetime.now().isoformat(timespec="seconds")
with open("app.log", "a") as f:
    f.write(f"{horodatage} {args.message}\n")
