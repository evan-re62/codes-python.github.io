# IA utilisé uniquement afin d'apprendre des fonctions que je ne connaissais pas, tel que "random.shuffle" ou "sys.exit()".

import random
import time 
import sys

CARTES = ['2 de Cœur', '3 de Cœur', '4 de Cœur', '5 de Cœur', '6 de Cœur', '7 de Cœur', '8 de Cœur', '9 de Cœur', '10 de Cœur', 
          'Valet de Cœur', 'Dame de Cœur', 'Roi de Cœur', 'As de Cœur', 
          '2 de Carreau', '3 de Carreau', '4 de Carreau', '5 de Carreau', '6 de Carreau', '7 de Carreau', '8 de Carreau', '9 de Carreau', '10 de Carreau',
          'Valet de Carreau', 'Dame de Carreau', 'Roi de Carreau', 'As de Carreau',
          '2 de Pique', '3 de Pique', '4 de Pique', '5 de Pique', '6 de Pique', '7 de Pique', '8 de Pique', '9 de Pique', '10 de Pique',
          'Valet de Pique', 'Dame de Pique', 'Roi de Pique', 'As de Pique',
          '2 de Trèfle', '3 de Trèfle', '4 de Trèfle', '5 de Trèfle', '6 de Trèfle', '7 de Trèfle', '8 de Trèfle', '9 de Trèfle', '10 de Trèfle',
          'Valet de Trèfle', 'Dame de Trèfle', 'Roi de Trèfle', 'As de Trèfle']

VALEURS_CARTES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
                  'Valet': 10, 'Dame': 10, 'Roi': 10, 'As': 11}

MAIN = []

MAIN_CROUPIER = []

CONTINUER = True


def calculer_score(main):
    score = 0
    nombre_as = 0

    for cartes in main:
        valeur_nom = cartes.split(" ")[0]
        score += VALEURS_CARTES[valeur_nom]

        if valeur_nom == 'As':
            nombre_as += 1

    while score > 21 and nombre_as > 0:
        score -= 10 
        nombre_as -= 1
    return score

def pioche_croupier():
    print(f"La main du croupier est : {MAIN_CROUPIER}")
    score_croupier = calculer_score(MAIN_CROUPIER)
    while score_croupier < 17:
        time.sleep(1)
        carte_piocher = CARTES.pop(0)
        MAIN_CROUPIER.append(carte_piocher)
        print(f"Le croupier à pioché la carte : {carte_piocher}")
        score_croupier = calculer_score(MAIN_CROUPIER)
    return score_croupier



print("Voulez-vous lancer une partie ? ")
DEMARRER = int(input("1 pour lancer une partie "))

if DEMARRER == 1:
    random.shuffle(CARTES)
    MAIN = [CARTES.pop(0) for i in range(2)]
    MAIN_CROUPIER = [CARTES.pop(0) for i in range(2)]
    print(f"\nLa première carte du croupier est : {MAIN_CROUPIER[0]} \n ")
    print(f"Votre mains contiens : {MAIN}\nVotre score est de : {calculer_score(MAIN)}\n")
else:
    print("Zéro risques hein")
    sys.exit()


while CONTINUER == True:
    print("Voulez-vous tirer (1) ou rester (0) ? \n")
    Choix = int(input("Votre choix : "))
    if  Choix == 0:
        CONTINUER = False
    elif Choix == 1:
        MAIN.append(CARTES.pop(0))
        print(f"Votre main contiens : {MAIN}\nVotre score est de : {calculer_score(MAIN)}\n")
        if calculer_score(MAIN) > 21:
            time.sleep(2)
            print(f"Votre score est égal à {calculer_score(MAIN)}, il est donc supérieur à 21 et vous avez alors perdu :(")
            sys.exit()
    else:
        print("Veuillez rentrer un choix valide.")
    

if CONTINUER == False:
    score_croupier = pioche_croupier()
    time.sleep(1)
    print(f"\n Le score du croupier est de : {score_croupier}")
    score_joueur = calculer_score(MAIN)
    time.sleep(1)
    print(f"\n Le score du joueur est de : {score_joueur}")
    time.sleep(1)
    if score_croupier < score_joueur or score_croupier > 21:
        print("\nVous avez gagné !!!")
    elif score_croupier == score_joueur:
        print("\nÉgalité !")
    else:
        print("\nVous avez perdu :(")





