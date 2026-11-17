import random

TABLE = [
  "01 Noir", "02 Rouge", "03 Noir",
  "04 Rouge", "05 Noir", "06 Rouge",
  "07 Noir", "08 Rouge", "09 Noir",
  "10 Rouge", "11 Noir", "12 Rouge",
  "13 Noir", "14 Rouge", "15 Noir",
  "16 Rouge", "17 Noir", "18 Rouge",
  "19 Noir", "20 Rouge", "21 Noir",
  "22 Rouge", "23 Noir", "24 Rouge",
  "25 Noir", "26 Rouge", "27 Noir",
  "28 Rouge", "29 Noir", "30 Rouge",
  "31 Noir", "32 Rouge", "33 Noir",
  "34 Rouge", "35 Noir", "36 Rouge"
]


def roulette():
    RESULTAT = None 
    RESULTAT = TABLE[random.randint(0, 35)]
    print(RESULTAT)
    return RESULTAT

def calculer_gain(choix, cases=None):



