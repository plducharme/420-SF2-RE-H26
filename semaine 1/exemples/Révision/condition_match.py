import math

reponse = int(input("Entrez un chiffre"))

match reponse:

    case 1:
        print("1")
    case 2:
        print("2")
    case _:
        print("Pas 1, pas 2")


print("a", "b", "c", sep="-->", end="\n\n")

print("Autre ligne")

print(math.tan(math.radians(45)))
