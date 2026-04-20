# fichier = open('citations.txt')
import sys

try:
    files = [open(f"./tmp/files-{n}.txt", "w") for n in range(10000)]
except OSError as ose:
    print(ose)

# Peut potentiellement générer un fichier corrompu
fichier = open('tst.txt', 'w')
fichier.write("Ceci est un test d'intégrité de fichier!")
sys.exit(1999)
