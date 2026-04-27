
class Manege:

    def __init__(self, nom: str, rayon_base: float, poids_chariots: float, vitesse_rotation: float):
        self.__rayon_base = rayon_base
        self.__poids_chariots = poids_chariots
        self.__vitesse_rotation = vitesse_rotation
        self.__nom = nom

    @property
    def rayon_base(self):
        return self.__rayon_base

    @rayon_base.setter
    def rayon_base(self, base):
        self.__rayon_base= base

    @property
    def poids_chariots(self):
        return self.__poids_chariots

    @poids_chariots.setter
    def poids_chariots(self, poids):
        self.__poids_chariots = poids

    @property
    def vitesse_rotation(self):
        return self.__vitesse_rotation

    @vitesse_rotation.setter
    def vitesse_rotation(self, vitesse):
        self.__vitesse_rotation = vitesse

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

