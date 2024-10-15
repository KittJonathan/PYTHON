import sys

if len(sys.argv) != 2:
    sys.exit("ERREUR : il faut exactement un argument.")

print(f"Argument vaut : {sys.argv[1]}")