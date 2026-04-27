import logging

# Configuration de base
# On spécifie le niveau DEBUG, WARNING, INFO, ERROR, CRITICAL
# Pour le format, plusieurs attributs sont disponibles, voir la section LogRecord Attributes de la documentation:
# https://docs.python.org/fr/3.14/library/logging.html#logrecord-attributes
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

logging.debug("Ce message n'apparaîtra pas car le niveau est à INFO")
logging.info("Message d'information")
logging.warning("Message d'avertissement")
logging.error("Message d'erreur")
logging.critical("Message critique")

# Une autre façon est d'utiliser le format par défaut au lieu d'appeler basicConfig()
logging.getLogger().setLevel(logging.INFO)
