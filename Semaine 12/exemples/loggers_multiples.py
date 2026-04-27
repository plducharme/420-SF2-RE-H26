import logging

# La fonction getLogger(nom) permet de retourner (il sera créer si inexistant) un logger associer au nom
console_logger = logging.getLogger("console")
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
console_logger.addHandler(console_handler)
console_logger.setLevel(logging.INFO)


# On va en créer un autre, vers un fichier cette fois-ci
fichier_logger = logging.getLogger("fichier log")
file_handler = logging.FileHandler("multiple_loggers.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
fichier_logger.addHandler(file_handler)
fichier_logger.setLevel(logging.WARNING)


for i in range(5):
    console_logger.info(f"i: {i}")
    fichier_logger.warning(f"La valeur de i est: {i}")
    fichier_logger.info("Fin de la boucle")


# getLogger(__name__) va retourner le logger par défaut pour ce module qui peut hériter d'un logger d'un niveau
# supérieur
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.info("Tout va bien!")
logger.debug("traces de debug pour trouver des problèmes ou lorsque l'on développe")