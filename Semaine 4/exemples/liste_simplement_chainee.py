class ListeSimplementChainee:
    # Le Noeud à la tête de la liste
    def __init__(self):
        self.__tete = None

    @property
    def tete(self):
        return self.__tete

    @tete.setter
    def tete(self, valeur: Noeud):
        self.__tete = valeur

    def inserer_tete(self, data):
        noeud = Noeud(data)
        # Si la tête existe, elle devient le suivant de la nouvelle tête
        if self.__tete is not None:
            noeud.suivant = self.tete
        self.__tete = noeud

    def inserer(self, index: int, valeur):
        compteur = 0
        nouveau_noeud = Noeud(valeur)
        courant: Noeud = self.__tete

        if index == 0:
            self.tete = nouveau_noeud
            return

        while courant is not None and compteur < index - 1:
            courant = courant.suivant
            compteur += 1

        if courant is None:
            raise ValueError("Index hors-limite")

        nouveau_noeud.suivant = courant.suivant
        courant.suivant = nouveau_noeud

    def inserer_fin(self, valeur):
        courant = self.__tete
        # On parcourt la liste jusqu'à ce qu'il n'y ait plus de suivant, puis on l'insère à la fin
        while courant.suivant is not None:
            courant = courant.suivant

        nouveau_noeud = Noeud(valeur)
        courant.suivant = nouveau_noeud

    def supprimer_debut(self):
        # On met le suivant en tête, le noeud supprimé sera ramassé par le ramasse-miettes
        tete = self.__tete
        suivant = tete.suivant
        self.__tete = suivant

    def supprimer_fin(self):
        noeud = self.__tete
        precedent = None
        # On parcours la liste jusqu'à ce qu'il n'y ait plus de suivant, toujours en gardant une référence vers le
        # précédent. Puis, on indique que le suivant du précédent est None
        while noeud.suivant is not None:
            precedent = noeud
            noeud = noeud.suivant

        precedent.suivant = None

    def supprimer(self, valeur):
        noeud: Noeud = self.__tete

        while noeud.suivant is not None and noeud.suivant.data != valeur:
            noeud = noeud.suivant
        if noeud.suivant is None:
            raise ValueError("Valeur introuvable")

        noeud.suivant = noeud.suivant.suivant


class Noeud:

    def __init__(self, valeur):
        self.__data = valeur
        self.__suivant = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valeur):
        self.__data = valeur

    @property
    def suivant(self):
        return self.__suivant

    @suivant.setter
    def suivant(self, valeur):
        self.__suivant = valeur


if __name__ == "__main__":
    lsc = ListeSimplementChainee()
    lsc.inserer_tete(3)
    lsc.inserer_tete(42)
    # avant la prochaine ligne, on a 42->3
    lsc.inserer(1, 666)
    # On a maintenant 42->666->3

    lsc.inserer_fin(999)
    # 42-666-3-999
    lsc.supprimer_debut()
    # 666-3-999
    lsc.supprimer_fin()
    # 666-3
    lsc.inserer_fin(333)
    lsc.inserer_fin(8)
    lsc.inserer_fin(64)
    # 666-3-333-8-64
    lsc.supprimer(333)

    lsc.supprimer(5555)
    print("")
