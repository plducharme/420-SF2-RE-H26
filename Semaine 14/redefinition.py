
class Bouffe:

    def __init__(self, nb_calories: int, nom: str):
        self._nb_calories = nb_calories
        self._nom = nom

    @property
    def nb_calories(self):
        return self._nb_calories

    @nb_calories.setter
    def nb_calories(self, nb_calories: int):
        self._nb_calories = nb_calories

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, nom: str):
        self._nom = nom

    def afficher_info(self):
        print(f"Nom:\t{self._nom}\nCalories:\t{self._nb_calories}")


class PateChinois(Bouffe):

    def __init__(self, nb_calories: int, nom: str, quantite: float):
        super().__init__(nb_calories, nom)
        self.__quantite = quantite

    @property
    def quantite(self) -> float:
        return self.__quantite

    @quantite.setter
    def quantite(self, quantite: float):
        self.__quantite = quantite

    def afficher_info(self):
        print(f"Nom:\t{self._nom}\nCal:\t{self._nb_calories}\nQté:\t{self.__quantite}")

    





