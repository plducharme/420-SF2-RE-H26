# Si on a une liste de int ou float, le sort se fait sur la valeur
liste_1 = [2, 42, 666, 98, 3, 5]
liste_1.sort()
print(liste_1)

# Si on a une liste de str, la valeurs des caractères est utlisée par le sorte
liste_2 = ["b", "a", "z", "e", "c", "bb"]
liste_2.sort()
print(liste_2)


# Si on a des objets, on doit indiquer la clé (la propriété) à utiliser
class Film:

    def __init__(self, annee_sortie: int, nom: str):
        self.__annee_sortie = None
        self.__nom = None
        self.annee_sortie = annee_sortie
        self.nom = nom

    @property
    def annee_sortie(self):
        return self.__annee_sortie

    @annee_sortie.setter
    def annee_sortie(self, valeur: int):
        if valeur < 0:
            raise ValueError("L'année ne peut pas être négative")
        self.__annee_sortie = valeur

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, valeur: str):
        self.__nom = valeur

    def __repr__(self):
        return f"Nom: {self.__nom} Année de sortie: {self.__annee_sortie}"


clockwork_orange = Film(1971, "A Clockwork Orange")
# film_bidon = Film(-45, "Film Bidon")
# print(film_bidon)

m_le_maudit = Film(1931, "M le maudit")
avatar_3 = Film(2025, "Avatar 3")

liste_films = [clockwork_orange, m_le_maudit, avatar_3]
liste_films.sort(key=lambda x: x.annee_sortie)
print(liste_films)
