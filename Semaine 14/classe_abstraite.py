from abc import ABC, abstractmethod


class ClasseAbstraite(ABC):

    @abstractmethod
    def methode_a_definir(self):
        pass


class ClasseEnfant1(ClasseAbstraite):

    def methode_a_definir(self):
        print("Mon implémentation pour enfant1")


class ClasseEnfant2(ClasseAbstraite):

    def methode_a_definir(self):
        print("Enfant 2: autre implémentation")


if __name__ == "__main__":
    enfant1 = ClasseEnfant1()
    enfant1.methode_a_definir()

    enfant2 = ClasseEnfant2()
    enfant2.methode_a_definir()
