from collections import deque

lettres_aleatoire = deque('adsfjfghjtyexcvbewq')
print(lettres_aleatoire)

# enlève et retourne l'élément au début de la liste
print(lettres_aleatoire.popleft())

# ajouter un élément à la fin
lettres_aleatoire.append('T')
print(lettres_aleatoire)

# recherche d'un élément dans la liste
print('j' in lettres_aleatoire)

# round robin
# rotate() décale les éléments d'un certain nombre de positions ; positif, vers la droite, négatif, vers la gauche
lettres_aleatoire.rotate(-1)
print(lettres_aleatoire)

lettres_aleatoire.rotate(3)
print(lettres_aleatoire)

# enlève et retourne l'élément de fin
print(lettres_aleatoire.pop())

# pour ajouter au début
lettres_aleatoire.appendleft("patate")
print(lettres_aleatoire)

# extendleft() ajoute les éléments d'une liste au début de la liste. Le premier élément de la liste est le premier à
# être ajouté à gauche
lettres_aleatoire.extendleft(["Bonjour", "les", "amis"])
print(lettres_aleatoire)

lettres_aleatoire.extend(["Vive", "la", "prog!"])
print(lettres_aleatoire)
