import json

# Afficher la valeur de la potion dans items.json
with open("items.json", mode="rt", encoding="utf8") as fichier_json:
    dict_items = json.load(fichier_json)
    # en une ligne
    print(dict_items["items"][0]["valeur"])
    # Détails
    liste_items = dict_items["items"]
    dict_premier_item = liste_items[0]
    valeur_premier_item = dict_premier_item["valeur"]
    print(valeur_premier_item)

# Afficher la statistique INT du héros dans heros.json
with open("heros.json", mode="rt", encoding="utf8") as fichier_heros:
    heros_dict = json.load(fichier_heros)
    print(heros_dict["stats"]["INT"])

