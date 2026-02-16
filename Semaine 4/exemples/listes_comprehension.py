# On déclare une expression qui va générer les valeurs suivie de conditions avec for ou if
cubes = [x**3 for x in range(12)]
print(cubes)
# équivalent
cubes = list(map(lambda x: x**3, range(12)))
print(cubes)
tuples_liste = [(x, y) for x in [4, 6, 9, 12] for y in [3, 8, 15, 11, 7] if x < y]
print(tuples_liste)
