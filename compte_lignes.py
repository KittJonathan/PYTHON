import sys

if len(sys.argv) != 2:
    sys.exit("ERREUR : il faut exactement un argument.")

nom_fichier = sys.argv[1]
taille = 0
with open(nom_fichier, "r") as f_in:
    taille = len(f_in.readlines())

print(f"{nom_fichier} contient {taille} lignes.")