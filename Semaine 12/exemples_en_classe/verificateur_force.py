from manege import Manege


def charger_maneges(nom_fichier: str) -> list[Manege]:
    maneges = []
    with open(nom_fichier, mode="rt", encoding="utf8") as input:
        for ligne in input:
            ligne_split = ligne.split()
            manege = Manege(ligne_split[0], float(ligne_split[1]), float(ligne_split[2]), float(ligne_split[3]))
            maneges.append(manege)
    return maneges


def calcul_force_centripete(manege: Manege) -> float:
    return manege.poids_chariots * (manege.vitesse_rotation / 3.6)**2 / manege.rayon_base


def verifier_securite_cable(resistance_cables: float, maneges: list[Manege]):
    for manege in maneges:
        force_centripete = calcul_force_centripete(manege)
        if resistance_cables < force_centripete:
            print(f"{manege.nom} n'est pas conforme. Force générée: {force_centripete:.2f} Résistance du cable:"
                  f" {resistance_cables}")
        else:
            print(f"{manege.nom} est conforme pour un cable de {resistance_cables}")


if __name__ == "__main__":
    liste_maneges_1 = charger_maneges("centripete.data")
    liste_maneges_2 = charger_maneges("centripete2.data")

    resistance_cable_a = 10000
    verifier_securite_cable(resistance_cable_a, liste_maneges_1)
    verifier_securite_cable(resistance_cable_a, liste_maneges_2)

    resistance_cable_acier = 50000
    verifier_securite_cable(resistance_cable_acier, liste_maneges_1)
    verifier_securite_cable(resistance_cable_acier, liste_maneges_2)


