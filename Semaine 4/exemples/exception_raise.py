# Pour lever une exception, on utilise le mot-clé "raise" suivi de l'exception que l'on veut lever
try:
    entier = input("Entrer un entier positif: ")
    mon_entier = int(entier)

    if mon_entier < 0:
        raise ValueError("Erreur: Entier négatif")
except TypeError as e:
    print(e)




