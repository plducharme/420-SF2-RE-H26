
def copier_fichier_texte(source: str, destination: str):
    contenu = []
    with open(source, mode="rt", encoding="utf8") as fichier_source:
        for ligne in fichier_source:
            contenu.append(ligne)

    with open(destination, mode="wt", encoding="utf8") as fichier_dest:
        for ligne in contenu:
            fichier_dest.write(ligne)


def copier_utf8_vers_ascii(source: str, destination: str):
    contenu = []
    with open(source, mode="rt", encoding="utf8") as fichier_source:
        contenu = fichier_source.readlines()
    with open(destination, mode="wt") as fichier_dest:
        for ligne in contenu:
            fichier_dest.write(str(ligne.encode(encoding="ascii")))


copier_fichier_texte("../citations.txt", "./cit2.txt")
copier_fichier_texte("../citations.txt", "./cit3.txt")

copier_utf8_vers_ascii("../citations.txt", "cit_ascii")
