# AUTEUR JK
from typing import Final

from scipy import constants

# CONSTANTES
TRILLION: Final = constants.exa
ZÉRO_ABSOLU: Final = -constants.zero_Celsius

# VARIABLES
température: float  # en degré

# LOGIQUE
température = int(input("Quelle est la température de l'eau ?"))

if température < ZÉRO_ABSOLU:
    print("Impossible, vérifiez la valeur saisie.")
elif température < 0:
    print("C'est de la glace.")
elif température < 100:
    print("C'est liquide.")
elif température < 2200:
    print("C'est gazeux")
elif température < 12e3: # notation scientifique
    print("C'est gazeux avec moins de 3% d'atomes libres.")
elif température < 4 * TRILLION:
    print("Gaz avec un certain % d'atomes libres.")
else:
    print("Ce n'est clairement plus de l'eau. "
          "C'est un gaz ionisé (plasma) d'hydrogène et d'oxygène.")
# ENDIF