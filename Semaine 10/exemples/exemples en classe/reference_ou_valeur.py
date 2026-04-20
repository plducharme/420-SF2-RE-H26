x = 10
y = 3
ma_liste = [3, 5, 7, 12, 78]


def changer_valeur(valeur: int):
    valeur = 42


# x ne sera pas changé, car il est passé par valeur
changer_valeur(x)
print(x)


def modifier_liste(liste: list):
    liste.append(42)


# La liste sera modifiée, car elle est passée par référence
modifier_liste(ma_liste)
print(ma_liste)


liste_1 = [1, 2, 3, 4, 5]
liste_2 = liste_1
liste_2.append(42)
print(liste_1)
