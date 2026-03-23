import math
from typing import Optional

# On peut suggérer les types attendus pour les paramètres et le retour des fonctions/méthodes
def pythagore(cote_adjacent: float, cote_oppose: float) -> float:
    return math.sqrt(cote_adjacent ** 2 + cote_oppose ** 2)


print(pythagore(3, 4))

pythagore([3, 4, 5], "patate")

# Pour typer les listes, on met le type attendu de la liste entre crochet
def trier(elements: list[int]):
    elements.sort()

# PyCharm va avertir si le type donné ne correspond pas au type attendu
trier(["1", "2", "3"])

# On peut aussi typer les variables dans le code
class Patate:

    def __init__(self, marque: str):
        self.marque: str = marque
        # Si on veut spécifier le type d'une variable qui est optionnelle
        self.couleur: Optional[str] = None

    # PyCharm va vous avertir que le type ne correspond pas
    def pousser(self):
        self.couleur = 1


def comparer_patates(elements: list[Patate]):
    pass