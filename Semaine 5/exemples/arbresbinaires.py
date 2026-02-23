# Arbre binaire de recherche (BST)
class Noeud:

    def __init__(self, valeur):
        # La valeur contenu dans ce noeud d'arbre (la clé)
        self.__valeur = valeur
        # Le fils de gauche (sera un objet de type Noeud ou None)
        self.__gauche = None
        # Le fils de droite (sera un objet de type Noeud ou None)
        self.__droite = None

    # Getter
    @property
    def valeur(self):
        return self.__valeur

    @property
    def gauche(self):
        return self.__gauche

    @property
    def droite(self):
        return self.__droite

    # Méthode qui insère en effectuant un tri
    # La méthode insertion permet de se comparer (self->noeud courant) avec le noeud que l'on veut inséré (celui en
    # paramètre)
    def insertion(self, noeud):
        # Si le noeud que l'on veut insérer est plus petit que le noeud courant
        if noeud.valeur < self.valeur:
            # Si le fils de gauche n'existe pas, le noeud à inséré devient le fils gauche
            if self.__gauche is None:
                self.__gauche = noeud
            # Si existant, on appelle la méthode insertion() sur le fils de gauche
            else:
                self.__gauche.insertion(noeud)
        # Si le noeud que l'on veut insérer est plus grand que le noeud courant
        else:
            # Si le fils de gauche n'existe pas, le noeud à inséré devient le fils droit
            if self.__droite is None:
                self.__droite = noeud
            # Si existant, on appelle la méthode insertion() sur le fils de droit
            else:
                self.__droite.insertion(noeud)

    # On effectue une recherche en profondeur. Le résultat donnera la liste des valeurs triées en ordre croissant
    def recherche_en_profondeur(self):
        # Si un fils gauche existe, on le visite en appelant recherche_en_profondeur()
        if self.__gauche is not None:
            self.__gauche.recherche_en_profondeur()
        #  On s'imprime
        print(f"{self.valeur} ", end="")
        # Si un fils droit existe, on le visite en appelant recherche_en_profondeur()
        if self.__droite is not None:
            self.__droite.recherche_en_profondeur()

    # Si on recherche une valeur, on regarde si le noeud existe ou si c'est le bon noeud; sinon, on recherche
    # recursivement en ustilisant le bon noeud fils
    @staticmethod
    def recherche(noeud: Noeud, valeur) -> bool:
        # Si le noeud n'existe pas, la valeur n'est par présente
        if noeud is None:
            return False
        # On regarde si le noeud courant est le bon. Dans ce cas on a trouvé la bonne valeur
        elif noeud.valeur == valeur:
            return True
        # Si la valeur recherchée est plus petite que le noeud courant, on doit chercher dans le fils gauche
        elif valeur < noeud.valeur:
            return Noeud.recherche(noeud.gauche, valeur)
        # Si la valeur de la clé est plus grande, on recherche dans le fils droit
        else:
            return Noeud.recherche(noeud.droite, valeur)


# Début du programme
if __name__ == "__main__":
    # Liste des items à insérer
    items = [6, 8, 2, 4, 0, 7, 3, 9]
    # La racine n'existe pas encore
    racine = None
    # On parcourt la liste des items pour les insérer, un par un, par la racine
    for item in items:
        # Si aucune racine existe, le noeud devient la racine
        if racine is None:
            # On créé le noeud racine en appelant le constructeur de Noeud avec l'item en paramètre. Le noeud va
            # contenir l'item
            racine = Noeud(item)
        # Sinon, on l'insère par la racine (en créer un Noeud) en appelant la méthode insertion(self, nouveau_noeud)
        else:
            racine.insertion(Noeud(item))
    # L'on affiche les items triés en effectuant une recherche en profondeur.
    racine.recherche_en_profondeur()
    print("")
    # On regarde si la valeur 8 existe
    print(f"Recherche 8: {Noeud.recherche(racine, 8)}")

    # On regarde si 10 existe
    print(f"Recherche 10: {Noeud.recherche(racine, 10)}")

