# Classe modélisant une expérience de physique électrique de base
class Potentiel:

    def __init__(self, resistance: float, intensite: float):
        self.__resistance = resistance
        self.__intensite = intensite

    @property
    def resistance(self):
        return self.__resistance

    @resistance.setter
    def resistance(self, valeur):
        self.__resistance = valeur

    @property
    def intensite(self):
        return self.__intensite

    @intensite.setter
    def intensite(self, valeur):
        self.__intensite = valeur

    def potentiel(self):
        return self.__resistance * self.__intensite

    def __repr__(self):
        return f"Potentiel: R:{self.__resistance} I:{self.intensite} U:{self.potentiel()}"

# Initialise un dictionnaire dont la clé est le nom de l'expérience et la valeur, l'objet Potentiel correspondant
# On lit les valeurs à partir du fichier electricite.txt
if __name__ == "__main__":
    experiences = {}
    with open("electricite.txt", mode="rt", encoding="utf8") as fichier_elec:
        for ligne in fichier_elec:
            ligne_split = ligne.split()
            potentiel = Potentiel(float(ligne_split[1]), float(ligne_split[2]))
            experiences[ligne_split[0]] = potentiel

    # Afficher le potentiel pour chaque expérience
    for cle, valeur in experiences.items():
        print(f"Expérience: {cle} potentiel: {valeur.potentiel()}")
