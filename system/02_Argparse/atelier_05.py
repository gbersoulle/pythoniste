import argparse

echelles = ["celsius", "fahrenheit", "kelvin"]

p = argparse.ArgumentParser()
p.add_argument("valeur", type=float)
p.add_argument("--from", dest="depuis", choices=echelles, required=True)
p.add_argument("--to",   dest="vers",   choices=echelles, required=True)
p.add_argument("--precision", type=int, default=2)
args = p.parse_args()

def vers_celsius(v, echelle):
    if echelle == "fahrenheit": return (v - 32) * 5 / 9
    if echelle == "kelvin":     return v - 273.15
    return v

def depuis_celsius(v, echelle):
    if echelle == "fahrenheit": return v * 9 / 5 + 32
    if echelle == "kelvin":     return v + 273.15
    return v

resultat = depuis_celsius(vers_celsius(args.valeur, args.depuis), args.vers)
prec = args.precision
print(f"{args.valeur:.{prec}f} {args.depuis} = {resultat:.{prec}f} {args.vers}")
