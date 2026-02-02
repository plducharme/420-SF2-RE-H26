class Sport:

    def __init__(self, nom: str):
        self._nom = nom

    def get_nom(self):
        return self._nom

    def set_nom(self, nom: str):
        self._nom = nom

    def info_sport(self):
        print(f"Nom: {self._nom}")


class Hockey(Sport):

    def __init__(self, duree: float, nb_joueurs_par_equipe: int):
        super().__init__("Hockey")
        self.__duree = duree
        self.__nb_joueurs_par_equipe = nb_joueurs_par_equipe

    def get_duree(self) -> float:
        return self.__duree

    def get_nb_joueurs_par_equipe(self) -> int:
        return self.__nb_joueurs_par_equipe

    def jouer(self):
        print("Le match commence")


hockey_rue = Hockey(120, 3)
hockey_lnh = Hockey(60, 23)

print(hockey_rue.get_nom())
hockey_rue.set_nom("Hockey de rue")
print(hockey_rue.get_nom())
hockey_lnh.jouer()
print(hockey_rue.get_nb_joueurs_par_equipe())


