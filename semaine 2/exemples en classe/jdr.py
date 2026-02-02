import random

class Entite:

    TYPE_MONSTRE = "Monstre"
    TYPE_HEROS = "Héros"
    TYPE_NPC = "NPC"

    def __init__(self, points_de_vie: int, type_entite: str, nom: str):
        self._points_de_vie = points_de_vie
        self._type = type_entite
        self._nom = nom

    def get_points_de_vie(self):
        return self._points_de_vie

    def get_nom(self):
        return self._nom


class Combattant(Entite):

    def __init__(self, points_de_vie, type_entite, nom, attaque, defense, armure):
        super().__init__(points_de_vie, type_entite, nom)
        self._attaque = attaque
        self._defense = defense
        self._armure = armure

    def attaquer(self, cible: Combattant):
        valeur_attaque = (self._attaque - cible._defense) * 100
        attaque_combattant = random.randint(1, 101)
        if attaque_combattant  < valeur_attaque:
            dommage = max(self._attaque - cible._armure, 2)
            print(f"{self._nom} a touché {cible._nom} pour {dommage} points de vie")
            cible._points_de_vie -= dommage
            print(f"{cible._nom} a {cible._points_de_vie} HP")




class Gobelin(Combattant):

    def __init__(self, nom):
        super().__init__(random.randint(5, 11), Entite.TYPE_MONSTRE, nom, random.randint(1, 6), 1, 0)


class Dragon(Combattant):

    def __init__(self, nom):
        super().__init__(150, Entite.TYPE_MONSTRE, nom, random.randint(10, 51), random.randint(10, 16), 25)


class Heros(Combattant):

    def __init__(self, nom):
        super().__init__(random.randint(75, 125), Entite.TYPE_HEROS, nom, random.randint(5, 20), random.randint(10, 15), 3)


class Jeu:

    def __init__(self, heros, npcs: list, nom_du_donjon):
        self.__nom_donjon = nom_du_donjon
        self.__heros: Heros = heros
        self.__npcs = npcs

    def jouer(self):
        while self.__heros.get_points_de_vie() > 0:
            print("On continue dans le donjon!")
            monstre = self.table_de_rencontre()
            print(f"Vous rencontrez {monstre.get_nom()}")

            while self.__heros.get_points_de_vie() > 0 and monstre.get_points_de_vie() > 0:
                self.__heros.attaquer(monstre)
                monstre.attaquer(self.__heros)

        print("Vous est mort! Recommencez!")

    def table_de_rencontre(self) -> Combattant:
        chance = random.randint(1, 101)
        monstre = None
        if chance == 100:
            monstre = Dragon("Igor")
        else:
            liste_noms = ["Arthur le Gobelin", "Karen", "Donald", "Roger"]
            monstre = Gobelin(random.choice(liste_noms))

        return monstre

nom_du_heros = input("Quel est votre nom? ")
heros = Heros(nom_du_heros)

jeu = Jeu(heros, [], "Donjon de Naheulbeuk")
jeu.jouer()







