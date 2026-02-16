# Si on n'utilise pas le mot-clé with
# f = open("test.txt", mode="r", encoding="utf-8")
# for ligne in f:
#     print(ligne, end="")
# f.close()

with open("test.txt", mode="r", encoding="utf-8") as fichier:
    for ligne in fichier:
        print(ligne, end="")
    print("")

# On gère l'exception
try:
    with open("test.pdf", mode="r") as fichier:
        for ligne in fichier:
            print(ligne, end="")
except FileNotFoundError as fnf:
    print(fnf)

# Va générer une exception non-gérée
with open("test.pdf", mode="r") as fichier:
    for ligne in fichier:
        print(ligne, end="")

