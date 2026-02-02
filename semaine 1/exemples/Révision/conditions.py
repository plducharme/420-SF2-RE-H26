# if elif....elif...else

chiffre = int(input("Entrez un chiffre"))
print(chiffre)

if chiffre == 1:
    print("C'est un 1")
elif 10 > chiffre > 0:
    print("plus petit que 10")
elif chiffre >= 10:
    print("10 ou plus")
else:
    print("Zéro ou moins")



