import csv


class ElementTableau:

    def __init__(self, no_atomique: int, symbole: str, nom: str, masse_atomique: float):
        self.__no_atomique = no_atomique
        self.__symbole = symbole
        self.__nom = nom
        self.__masse_atomique = masse_atomique

    @property
    def no_atomique(self):
        return self.__no_atomique

    @no_atomique.setter
    def no_atomique(self, numero: int):
        self.__no_atomique = numero

    @property
    def symbole(self):
        return self.__symbole

    @symbole.setter
    def symbole(self, symbole: str):
        self.__symbole = symbole

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def masse_atomique(self):
        return self.__masse_atomique

    @masse_atomique.setter
    def masse_atomique(self, masse: float):
        self.__masse_atomique = masse

    def __repr__(self):
        return f"{self.no_atomique}, {self.symbole}, {self.nom}, {self.masse_atomique}"


with open("PubChemElements_all.csv", mode="rt", encoding="utf8") as fichier_csv:
    elements_csv = csv.DictReader(fichier_csv)
    liste_elements_tableau = []
    for element in elements_csv:
        liste_elements_tableau.append(ElementTableau(int(element["AtomicNumber"]), element["Symbol"], element["Name"],
                                                     float(element["AtomicMass"])))


for element_tableau in liste_elements_tableau:
    print(element_tableau)

