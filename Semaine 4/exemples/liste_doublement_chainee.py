class ListeDoublementChainee:

    def __init__(self):
        self.__tete = None
        self.__queue = None

    @property
    def tete(self):
        return self.__tete

    @tete.setter
    def tete(self, valeur):
        self.__tete = valeur

    @property
    def queue(self):
        return self.__queue

    @queue.setter
    def queue(self, valeur):
        self.__queue = valeur

    def inserer_tete(self, valeur):
        nouveau_noeud = Noeud(valeur)
        # Dans le cas que la liste est vide, le nouveau noeud deviendra la tete et la queue
        if self.__tete is None:
            self.__tete = nouveau_noeud
            self.__queue = nouveau_noeud
            return

        tete = self.__tete
        tete.precedent = nouveau_noeud
        nouveau_noeud.suivant = tete
        self.__tete = nouveau_noeud

    def inserer_queue(self, valeur):
        nouveau_noeud = Noeud(valeur)
        # Dans le cas que la liste est vide, le nouveau noeud deviendra la tete et la queue
        if self.__queue is None:
            self.__tete = nouveau_noeud
            self.__queue = nouveau_noeud
            return

        queue = self.__queue
        queue.suivant = nouveau_noeud
        nouveau_noeud.precedent = queue
        self.queue = nouveau_noeud

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

    def supprimer_tete(self):
        tete = self.tete
        # On va chercher l'élément suivant la tête actuelle
        suivant: Noeud = tete.suivant
        # On assigne au suivant le précédent comme None
        suivant.precedent = None
        # La tete devient le suivant
        self.tete = suivant

    def supprimer_queue(self):

        queue = self.queue
        # On va chercher l'élément précédent la queue actuelle
        precedent: Noeud = queue.precedent
        # On assigne au précédent le suivant comme étant None
        precedent.suivant = None
        # La queue devient le précédent
        self.queue = precedent

    def supprimer(self, valeur):
        noeud: Noeud = self.__tete

        while noeud.suivant is not None and noeud.suivant.data != valeur:
            noeud = noeud.suivant
        if noeud.suivant is None:
            raise ValueError("Valeur introuvable")

        noeud.suivant = noeud.suivant.suivant

    # transforme en une liste python
    def tolist(self):
        liste_python = []
        courant: Noeud = self.tete
        while courant is not None:
            liste_python.append(courant.valeur)
            courant = courant.suivant
        return liste_python



class Noeud:

    def __init__(self, data):
        self.__data = data
        self.__suivant = None
        self.__precedent = None

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

    @property
    def precedent(self):
        return self.__precedent

    @precedent.setter
    def precedent(self, valeur):
        self.__precedent = valeur


if __name__ == "__main__":
    ldc = ListeDoublementChainee()

    ldc.inserer_tete(42)
    ldc.inserer_tete(666)
    ldc.inserer_tete(3)
    # 3-666-42


    print("")