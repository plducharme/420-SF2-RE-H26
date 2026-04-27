import pickle
from voiture import Voiture

challenger = Voiture("Dodge", "Challenger SRT8", 2014, 150000)

with open("voiture.pickle", mode="wb") as fichier_pickle:
    pickle.dump(challenger, fichier_pickle)

with open("voiture.pickle", mode="rb") as pickle_input:
    ma_voiture = pickle.load(pickle_input)

print("Voiture originale")
print(challenger)
print("Voiture désérialisée")
print(ma_voiture)

print("On avance le Challenger")
challenger.avancer(5, 70)

if challenger != ma_voiture:
    print("Ne sont plus égaux")
    print(challenger)
    print(ma_voiture)
