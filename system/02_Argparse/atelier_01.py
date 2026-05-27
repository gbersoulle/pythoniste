import argparse, sys

p = argparse.ArgumentParser()
p.add_argument("a", type=float)
p.add_argument("op", choices=["+", "-", "*", "/"])
p.add_argument("b", type=float)
args = p.parse_args()

if args.op == "/" and args.b == 0:
    print("Erreur : division par zéro", file=sys.stderr)
    sys.exit(1)

ops = {"+": args.a + args.b, "-": args.a - args.b,
       "*": args.a * args.b, "/": args.a / args.b}
print(f"{args.a} {args.op} {args.b} = {ops[args.op]}")
