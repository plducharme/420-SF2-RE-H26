from arbresbinaires import Noeud
import csv
import random


class Element:

    def __init__(self, symbole: str, no_atomique: int):
        self.__symbole = symbole
        self.__no_atomique = no_atomique

    @property
    def symbole(self):
        return self.__symbole

    @property
    def no_atomique(self):
        return self.__no_atomique

    def __lt__(self, other):
        return self.no_atomique < other.no_atomique

    def __repr__(self):
        return f"Element {self.symbole} {self.no_atomique}"


if __name__ == "__main__":


    liste_elements = []

    with open("./data/tableauperiodique.csv", mode="r", encoding="utf8") as fichier_csv:

        lecteur_csv = csv.DictReader(fichier_csv)
        for ligne in lecteur_csv:
            liste_elements.append(Element(ligne["Symbol"], int(ligne["AtomicNumber"])))

    random.shuffle(liste_elements)

    racine: Noeud = Noeud(liste_elements[0])

    for i in range(1, len(liste_elements) - 1):
        racine.insertion(Noeud(liste_elements[i]))

    racine.recherche_en_profondeur()

