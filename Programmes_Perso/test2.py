import random

TABLE = [     "0 Vert",
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
    RESULTAT = TABLE[random.randint(0, 36)]
    print(RESULTAT)
    return RESULTAT

def calculer_gain(RESULTAT, choix, Solde, Mise, cases=None):
    Solde -= Mise
    gain = 0
    if choix == "Rouge":
      if RESULTAT.split(" ")[1] == choix:
        gain += Mise*2
    elif choix == "Noir":
      if RESULTAT.split(" ")[1] == choix:
        gain += Mise*2
    elif RESULTAT.split(" ")[0] == choix.split(" ")[0]:
      gain += Mise*35
    elif choix == "Colonne 1":
      if RESULTAT in [TABLE[1 + 3*i] for i in range(12)]:
        gain += Mise*2.5
    elif choix == "Colonne 2":
      if RESULTAT in [TABLE[2 + 3*i] for i in range(12)]:
        gain += Mise*2.5
    elif choix == "Colonne 3":
      if RESULTAT in [TABLE[3 + 3*i] for i in range(12)]:
        gain += Mise*2.5
    elif choix == "Cheval" and cases != None:
      chevaux_valides = (
          [[TABLE[i], TABLE[i + 1], TABLE[i + 3], TABLE[i + 4]] for i in range(1, 33) if i % 3 != 0] )
      if sorted(cases) in chevaux_valides and RESULTAT in cases:
        print(chevaux_valides)
        gain += Mise*18
    Solde += gain
    return Solde, chevaux_valides, cases

       
print(calculer_gain(roulette(), "Cheval", 100, 20, ["0 Vert", "01 Noir", "02 Rouge", "03 Noir"]))