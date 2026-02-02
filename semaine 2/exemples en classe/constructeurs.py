# Exemple d'une classe avec un constructeur par défaut (il l'hérite de object)
class Mobile:

    pass

# L'appel du constructeur par défaut est fait implicitement
mobile1 = Mobile()


# Exemple d'une classe avec un constructeur paramétré
class Nourriture:

    def __init__(self, nom: str, gout: str, calories_moyennes: int):
        self.__nom = nom
        self.__gout = gout
        self.__calories_moyennes = calories_moyennes

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_gout(self):
        return self.__gout

    def get_calories_moyennes(self):
        return self.__calories_moyennes

    def set_calories_moyennes(self, calories_moyennes: int):
        self.__calories_moyennes = calories_moyennes


big_mac = Nourriture("Big Mac", "McDo", 800)
print(big_mac.get_nom())
big_mac.set_nom("Le Big Mac")


