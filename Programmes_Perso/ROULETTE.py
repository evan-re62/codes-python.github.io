import random
import time

type_mise = ["Rouge", "Noir", "Colonne 1", "Colonne 2", "Colonne 3", "Cheval", "Transversal", "Carré", "Impair", "Pair", "Manque", "Passe", "D12", "M12", "P12", "Sixain", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
              "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"
]

TABLE =[
              "00 Vert",
  "01 Rouge", "02 Noir",  "03 Rouge",
  "04 Noir",  "05 Rouge", "06 Noir",
  "07 Rouge", "08 Noir",  "09 Rouge",
  "10 Noir",  "11 Noir",  "12 Rouge",
  "13 Noir",  "14 Rouge", "15 Noir",
  "16 Rouge", "17 Noir",  "18 Rouge",
  "19 Rouge", "20 Noir",  "21 Rouge",
  "22 Noir",  "23 Rouge", "24 Noir",
  "25 Rouge", "26 Noir",  "27 Rouge",
  "28 Noir",  "29 Noir",  "30 Rouge",
  "31 Noir",  "32 Rouge", "33 Noir",
  "34 Rouge", "35 Noir",  "36 Rouge"
]

sixain_valides = (
        [[TABLE[i], TABLE[i +1], TABLE[i + 2],TABLE[i + 3], TABLE[i +4], TABLE[i + 5]] for i in range(1, 36, 3)]) 
print(sixain_valides) 

def roulette():
    RESULTAT = None 
    RESULTAT = TABLE[random.randint(0, 36)]
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
    elif choix == "Impair":
      if int(RESULTAT.split(" ")[0]) % 2 != 0:
        gain += Mise*2
    elif choix == "Pair":
      if int(RESULTAT.split(" ")[0]) % 2 == 0:
        gain += Mise*2
    elif choix == "Manque":
      if 1 <= int(RESULTAT.split(" ")[0]) <= 19:
        gain += Mise*2
    elif choix == "Passe":
      if 19 <= int(RESULTAT.split(" ")[0]) <= 36 :
        gain += Mise*2
    elif choix == "P12":
      if 1 <= int(RESULTAT.split(" ")[0]) <= 12:
        gain += Mise*3
    elif choix == "M12":
      if 13 <= int(RESULTAT.split(" ")[0]) <= 24:
        gain += Mise*3
    elif choix == "D12":
      if 25 <= int(RESULTAT.split(" ")[0]) <= 36:
        gain += Mise*3
    elif RESULTAT.split(" ")[0] == choix.split(" ")[0]:
      gain += Mise*35
    elif choix == "Colonne 1":
      if RESULTAT in [TABLE[1 + 3*i] for i in range(12)]:
        gain += Mise*3
    elif choix == "Colonne 2":
      if RESULTAT in [TABLE[2 + 3*i] for i in range(12)]:
        gain += Mise*3
    elif choix == "Colonne 3":
      if RESULTAT in [TABLE[3 + 3*i] for i in range(12)]:
        gain += Mise*3
    elif choix == "Cheval" and cases != None:
      chevaux_valides = (
          [[TABLE[0], TABLE[i]] for i in (1, 2, 3)] +
          [[TABLE[i], TABLE[i + 1]] for i in range(1, 36) if i % 3 != 0] +
          [[TABLE[i], TABLE[i + 3]] for i in range(1, 34)]
      )
      if sorted(cases) in chevaux_valides and RESULTAT in cases:
        gain += Mise*18
    elif choix == "Transversal" and cases != None:
      transver_valides = (
        [TABLE[0:3]] +
        [[TABLE[i], TABLE[i +1], TABLE[i + 2]] for i in range(1, 36, 3)] )
      if sorted(cases) in transver_valides and RESULTAT in cases:
        gain += 12*Mise
    elif choix == "Sixain" and cases != None:
      sixain_valides = (
        [[TABLE[i], TABLE[i +1], TABLE[i + 2],TABLE[i + 3], TABLE[i +4], TABLE[i + 5]] for i in range(1, 36, 6)]) 
      print(sixain_valides)  
      if sorted(cases) in sixain_valides and RESULTAT in cases:
        gain += 7*Mise
    elif choix == "Carré" and cases != None:
      carrés_valides = (
        [TABLE[0:4]] +
        [[TABLE[i], TABLE[i + 1], TABLE[i + 3], TABLE[i + 4]] for i in range(1, 33) if i % 3 != 0] )
      if sorted(cases) in carrés_valides and RESULTAT in cases:
        gain += Mise*9
    Solde += gain
    return Solde, gain

def jeu():
  solde = 1000
  mise = 0
  cases = []
  nb_game = 0
  while True:
    if solde <= 0:
      break

    elif nb_game > 0:
      choix = input("Voulez-vous arrêter ? ('Oui' pour arrêter) ")
      if choix.lower() == "oui":
        break

    print("Bienvenue au jeu de la roulette ! \n")
    print(f"              {TABLE[0]}  ")
    for i in range(1, 36, 3):
      print(f"{TABLE[i]:<14}{TABLE[i + 1]:<14}{TABLE[i + 2]}")
    choix = input("Votre choix de type de mise : ")
    if choix not in type_mise:
      print("Ce type de mise n'existe pas")
      break
    roue = roulette()
    mise = int(input("Combiens misez-vous :"))
    if choix == "Cheval":
      for i in range(2):
        case = input("Choix de la case : ")
        cases.append(case)
      solde, gain = calculer_gain(roue, choix, solde, mise, cases)
    elif choix == "Transversal":
        for i in range(3):
          case = input("Choix de la case : ")
        cases.append(case)
        solde, gain = calculer_gain(roue, choix, solde, mise, cases)

    elif choix == "Carré":
      for i in range(4):
        case = input("Choix de la case : ")
        cases.append(case)
      solde, gain = calculer_gain(roue, choix, solde, mise, cases)
        
    else:
      solde, gain = calculer_gain(roue, choix, solde, mise)
    for i in range(100):
      print(TABLE[random.randint(0, 36)], end="\r")
      time.sleep(0.09)
    print(f"Résultat de la roue : {roue}")
    time.sleep(1)
    print(f"Vous avez gagner : {gain - mise}$")
    print(f"Il vous reste : {solde}$")
    nb_game += 1  
        





jeu()