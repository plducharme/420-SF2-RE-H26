class Athlete:

    # Constructeur
    def __init__(self, age: int, nom: str, sport: str):
        self.age = age
        self.nom = nom
        self.sport = sport

    def __lt__(self, other):
        if self.age < other.age:
            return True
        return False

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


mbappe = Athlete(27, "Kylian Mbappe", "soccer")
jornet = Athlete(41, "Kylian Jornet", "course")

if mbappe < jornet:
    print("plus jeune")

# python fait ceci sous le capot, l'implémentation de l'opérateur est donc celle de l'objet mbappe
if mbappe.__lt__(jornet):
    print("plus jeune")


class Item:

    def __init__(self, quantite, prix, sku):
        self.quantite = quantite
        self.prix = prix
        self.sku = sku

    def __add__(self, other):
        if self.sku != other.sku:
            raise ValueError("Erreur: pas les mêmes SKU")
        return Item(self.quantite + other.quantite, self.prix, self.sku)

    def __str__(self):
        return f"SKU [{self.sku}, qte: {self.quantite}, prix: {self.prix}]"


item1 = Item(5, 5.25, 123456)
item2 = Item(3, 6.75, 654321)
item3 = Item(10, 5.25, 123456)

item_1_3 = item1 + item3
print(item_1_3)

item_1_2 = item1 + item2
