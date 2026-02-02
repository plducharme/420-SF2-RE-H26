import math

def nom_de_la_fonction(parametre1, parametre2, **parametres_nommes):
    print(parametre1, parametre2, parametres_nommes)

# Appel de la fonction avec des paramètres et des paramètres nommés
nom_de_la_fonction(1, 2, toto=3, couleur="rouge")

def pythagore_avec_params(adjacent, oppose):
    return math.sqrt(adjacent ** 2 + oppose**2), adjacent, oppose

hypo, adj, opp = pythagore_avec_params(3, 4)


