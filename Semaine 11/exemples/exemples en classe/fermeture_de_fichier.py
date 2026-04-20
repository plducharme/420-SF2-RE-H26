
# Fermeture manuel
mon_fichier = open("fermeture_manuel.txt", mode="w", encoding="utf8")
mon_fichier.write("Ceci est un test!")
mon_fichier.write("On continue d'écrire")
mon_fichier.close()

# Bloc finally manuel
fichier = open("bloc_finally.txt", mode="w", encoding="utf8")
try:
    fichier.write("Carpe Diem!")
except OSError as ose:
    print(ose)
finally:
    fichier.close()


# Ouverture avec un with pour fermeture automatique
with open("fichier_with.txt", mode="w", encoding="utf8") as fichier_with:
    fichier_with.write("Ceci est un nouveau fichier!\nLet's go!")
    liste_chars = []
    for i in range(128, 1025):
        liste_chars.append(chr(i))
    fichier_with.writelines(liste_chars)







