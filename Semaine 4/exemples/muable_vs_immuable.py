# Une structure de données qui est muable peut être modifiée après sa déclaration
# Ex: les listes
ma_liste = [1, 2, 3, 4]
ma_liste.append(42)
ma_liste.remove(2)
print(ma_liste)

# Une structure de données qui est immuable va générer une erreur à la réaffectation ou la modification
mon_tuple = (1, 2, 3, 4)
mon_tuple[2] = 42
