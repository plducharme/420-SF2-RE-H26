class Film:

    def __init__(self, titre: str, annee: int, auteur: str, duree: float):
        self.titre = titre
        self.annee = annee
        self.auteur = auteur
        self.duree = duree

    def info(self):
        print(f"Le film {self.titre} est sorti en {self.annee} et dure {self.duree} minutes")



the_shining = Film("The Shining", 1980, "Stanley Kubrick", 120)
the_shining.info()



avatar = Film("Avatar: The last air bender", 2005, "Michael DiMartino", 115)
avatar.info()



