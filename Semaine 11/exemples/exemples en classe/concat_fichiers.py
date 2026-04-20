def concatenation_fichiers(destination: str, *fichiers: str):
    for fichier in fichiers:
        with open(fichier, mode="rt", encoding="utf8") as f:
            with open(destination, mode="at", encoding="utf8") as ecriture:
                ecriture.write(f.read())


concatenation_fichiers("bella_ciao.txt", "source1.txt", "source2.txt", "source3.txt")


