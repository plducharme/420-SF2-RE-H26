# Déclaration d'un tuple
coord = (4, 5)

print(coord[0])
print(coord[1])


def fonction1():
    return 7, 8, 9


x, y, z = fonction1()


def fonction2(*args):
    print(args)
    for valeur in args:
        print(valeur)


fonction2(9, 8, 7, 6, 5)





