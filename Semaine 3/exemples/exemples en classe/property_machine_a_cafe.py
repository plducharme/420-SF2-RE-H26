class MachineACafe:

    def __init__(self, marque: str, nb_de_gradation: int, temperatures_eau: list[float]):
        self.__marque = marque
        self.__nb_de_gradation = nb_de_gradation
        self.__temperatures_eau = temperatures_eau

    @property
    def marque(self):
        print("Getter marque() appelé")
        return self.__marque

    @marque.setter
    def marque(self, marque: str):
        self.__marque = marque

    @property
    def nb_de_gradation(self):
        return self.__nb_de_gradation

    @nb_de_gradation.setter
    def nb_de_gradation(self, nb_gradation: int):
        self.__nb_de_gradation = nb_gradation

    @property
    def temperatures_eau(self):
        return self.__temperatures_eau

    @temperatures_eau.setter
    def temperatures_eau(self, temperatures: list[float]):
        self.__temperatures_eau = temperatures


ninja = MachineACafe("Ninja", 5, [95.0, 100.0, 115.0])
print(ninja.marque)
ninja.marque = "Cuisinart"
ninja.temperatures_eau.append(85.0)


# Pour comparer avec des getters setters classiques
class MachineACafeClassique:

    def __init__(self, marque: str, nb_de_gradation: int, temperatures_eau: list[float]):
        self.__marque = marque
        self.__nb_de_gradation = nb_de_gradation
        self.__temperatures_eau = temperatures_eau

    def get_marque(self) -> str:
        return self.__marque

    def set_marque(self, marque: str):
        self.__marque = marque

    def get_nb_de_gradation(self):
        return self.__nb_de_gradation

    def set_nb_de_gradation(self, nb_gradation : int):
        self.__nb_de_gradation = nb_gradation

    def get_temperatures_eau(self):
        return self.__temperatures_eau

    def set_temperatures_eau(self, temperatures: list[float]):
        self.__temperatures_eau = temperatures


ninja2 = MachineACafeClassique("Ninja", 5, [95.0, 100.0, 115.0])
print(ninja2.get_marque())
ninja2.set_marque("Cuisinart")
ninja2.get_temperatures_eau().append(85.0)











