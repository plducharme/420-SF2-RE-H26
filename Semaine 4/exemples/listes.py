instruments = ['guitare', 'basse', 'mandoline', 'banjo', 'piano', 'guitare']
ma_liste_2 = list((1, 2, 3, 4))
print(ma_liste_2)
# compter le nombre de 'guitare'
print(instruments.count('guitare'))

# index de banjo
print(instruments.index('banjo'))

# index de guitare à partir du début
print(instruments.index('guitare'))
# index de guitare à partir de la position 2
print("Index de guitare à partir de l'index 2")
print(instruments.index('guitare', 2))

# renverse l'ordre de la liste
instruments.reverse()
print(instruments)

# ajoute un élément à la fin de la liste
instruments.append('cornemuse')
print(instruments)



