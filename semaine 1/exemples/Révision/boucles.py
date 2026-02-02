for i in range(1, 9):
    print(i)


arret = False
compteur = 1
while not arret:
    print("boucle")
    if compteur == 6:
        arret = True
    compteur += 1
print("Hors de la boucle")

while True:
    reponse = input("Voulez-vous arrêter?")
    if reponse == "O":
        break
    elif reponse == "N":
        print("On va continuer")
    else:
        print("Réponse inconnue, on continue")
        continue


