import random
from time import perf_counter_ns

# On va se générer une liste d'éléments au hasard
elements = [random.randint(0, 1000000) for _ in range(500001)]
print(f"Longueur de la liste {len(elements)}")
# l'ensemble va aussi enlever les doublons
debut = perf_counter_ns()
ensemble_elements = set(elements)
total = perf_counter_ns()
print(f"Longueur de l'ensemble {len(ensemble_elements)}")
print(f"Temps pour créer l'ensemble {total - debut} nanosecondes")

# on teste si certaines valeurs appartiennent à la liste ou à l'ensemble
debut = perf_counter_ns()
present = 42 in elements
total = perf_counter_ns() - debut
print(f"Test si 42 est dans la liste: {present} {total} nanoseconds")

debut = perf_counter_ns()
present = 42 in ensemble_elements
total = perf_counter_ns() - debut
print(f"Test si 42 est dans l'ensemble: {present} {total} nanoseconds")

# Ici pour une démonstration plus impressionnante, on utilise une valeur que l'on sait non-présente (voir le range())
# Pour la liste, toute la liste devra être parcourue.
debut = perf_counter_ns()
present = 1800000 in elements
total = perf_counter_ns() - debut
print(f"Test si 1800000 est dans la liste: {present} {total} nanoseconds")

debut = perf_counter_ns()
present = 1800000 in ensemble_elements
total = perf_counter_ns() - debut
print(f"Test si 1800000 est dans l'ensemble: {present} {total} nanoseconds")
