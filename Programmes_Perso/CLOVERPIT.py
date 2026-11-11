import random
import time
import copy
import sys

SYMBOLES = ["🍋", "🍒", "🍀", "🔔", "💎", "📦", "⭐"]

POURCENTAGE = [19.4, 19.4, 14.9, 14.9, 11.9, 11.9, 7.5]

VALEURS_SYMBOLES = {"🍋": 2, "🍒": 2, "🍀": 3,
                    "🔔": 3, "💎": 5, "📦": 5, "⭐": 7}

MULTIPLICATEURS_FORME = {"Hor": 1, "Vert": 1, "Diag": 1, "Hor-L": 2, "Hor-XL": 3, 
                         "Zig": 4, "Zag": 4, "Above": 7, "Below": 7, "Eye": 8, "JACKPOT": 10} 

def calculer_gain(grille):
    gain = 0

    for ligne in grille:
        if ligne[0] == ligne[1] == ligne[2] == ligne[3] == ligne[4]:
            gain += VALEURS_SYMBOLES[ligne[0]] * 5 * MULTIPLICATEURS_FORME["Hor-XL"]
        elif ligne[0] == ligne[1] == ligne[2] == ligne[3] or ligne[1] == ligne[2] == ligne[3] == ligne[4]:
            gain += VALEURS_SYMBOLES[ligne[2]] * 4 * MULTIPLICATEURS_FORME["Hor-L"]
        elif ligne[0] == ligne[1] == ligne[2] or ligne[1] == ligne[2] == ligne[3] or ligne[2] == ligne[3] == ligne[4]:
            gain += VALEURS_SYMBOLES[ligne[2]] * 3 * MULTIPLICATEURS_FORME["Hor"]
            
    for i in range(5):
        if grille[0][i] == grille[1][i] == grille[2][i]:
            gain += VALEURS_SYMBOLES[grille[0][i]] * 3 * MULTIPLICATEURS_FORME["Vert"]
    for i in range(3):
        if grille[0][i] == grille[1][i+1] == grille[2][i+2]:
            gain += VALEURS_SYMBOLES[grille[0][i]] * 3 * MULTIPLICATEURS_FORME["Diag"]
    for i in range(3):
            if grille[2][i] == grille[1][i+1] == grille[0][i+2]:
                gain += VALEURS_SYMBOLES[grille[2][i]] * 3 * MULTIPLICATEURS_FORME["Diag"]

    if grille[0][2] == grille[1][1] == grille[1][3] == grille[2][0] == grille[2][4]:
        gain += VALEURS_SYMBOLES[grille[0][2]] * 5 * MULTIPLICATEURS_FORME["Zig"]

    if grille[0][0] == grille[0][4] == grille[1][1] == grille[1][3] == grille[2][2]:
            gain += VALEURS_SYMBOLES[grille[0][0]] * 5 * MULTIPLICATEURS_FORME["Zag"]
    if grille[0][2] == grille[1][1] == grille[1][3] == grille[2][0] == grille[2][1] == grille[2][2] == grille[2][3] == grille[2][4]:
         gain += VALEURS_SYMBOLES[grille[0][2]] * 8 * MULTIPLICATEURS_FORME["Above"]
    if grille[0][0] == grille[0][1] == grille[0][2] == grille[0][3] == grille[0][4] == grille[1][1] == grille[1][3] == grille[2][2]:
         gain += VALEURS_SYMBOLES[grille[0][0]] * 8 * MULTIPLICATEURS_FORME["Below"]
    if grille[0][1] == grille[0][2] == grille[0][3] == grille[1][0] == grille[1][1] == grille[1][3] == grille[1][4] == grille[2][1] == grille[2][2] == grille[2][3]:
         gain += VALEURS_SYMBOLES[grille[0][1]] * 10 * MULTIPLICATEURS_FORME["Eye"]
    for ligne in grille:
        if all(case == grille[0][0] for ligne in grille for case in ligne):
            gain += VALEURS_SYMBOLES[ligne[0]] * 15 * MULTIPLICATEURS_FORME["JACKPOT"]
            
    return gain


def jeu():
    dette = 100
    deposer = 30
    tour_restant = 4
    argent = 14

    while True:
        print(f"\nDette = {dette}")
        print(f"\nArgent deposer = {deposer}")
        print(f"\nTours restants = {tour_restant}")
        print("\nQue voulez-vous faire ?\n 1. Jouer\n 2. Déposer\n 3. Les symboles")
        print(f"Vous avez {int(argent)}$")
        choix = input("")

        if choix == "1":
            if tour_restant > 0:
                if argent >= 3:
                 
                    print("\nVoulez vous faire 7 roue, ou 3 ?")
                    nb_roue = int(input(""))
                    if nb_roue == 7:
                        argent -= 7
                        for i in range(7):
                            time.sleep(2)
                            print(f"Grille numéro {i+1}")
                            print(" ")
                            grille = [[random.choices(SYMBOLES, weights=POURCENTAGE, k=1)[0] for _ in range(5)] for _ in range(3)]
                            for ligne in grille:
                                print(*ligne)
                                time.sleep(0.5)
                            argent_preced = copy.copy(argent)
                            argent += calculer_gain(grille)
                            print(f"\nVous avez gagner {int(argent - argent_preced)}\n")
                        tour_restant -= 1
                        argent += int(deposer * 1.07 - deposer)
                        print(f"\nVous avez gagnez vos intérêts : {int(deposer * 1.07 - deposer)}$")
                        
                    if nb_roue == 3:
                        argent -= 3
                        for i in range(3):
                            time.sleep(2)
                            print(f"Grille numéro {i+1}")
                            print(" ")
                            grille = [[random.choices(SYMBOLES, weights=POURCENTAGE, k=1)[0] for _ in range(5)] for _ in range(3)]
                            for ligne in grille:
                                print(*ligne)
                                time.sleep(0.5)
                            argent_preced = copy.copy(argent)
                            argent += calculer_gain(grille)
                            print(f"\nVous avez gagner {int(argent - argent_preced)}\n")
                        tour_restant -= 1
                        argent += int(deposer * 1.07 - deposer)
                        print(f"\nVous avez gagnez vos intérêts : {int(deposer * 1.07 - deposer)}$")
                
            else:
                print("Vous n'avez plus de tirage de disponible")


        if choix == "3":
                print("Les symboles et leurs chances d'appartions et valeurs")
                print(f"{SYMBOLES}\n{POURCENTAGE}\n")
                print(f"{VALEURS_SYMBOLES}")
                
        
        if choix == "2":
            print("Combiens vouslez vous déposer ?")
            thune = int(input(""))
            if thune <= argent:
                deposer += thune
                argent -= thune
                print(f"\nIl reste {int(dette - deposer)}$ à déposer pour passer au prochain tour")
            else:
                print("Veuillez entré une somme inférieur ou égale à la votre.")

        if tour_restant == 0 and deposer + argent < dette:
            print("Malheureusement, vous ne pouvez plus payer vos dettes. Vous êtes éliminé.")
            sys.exit()
        elif dette <= deposer and tour_restant == 4:
            print("Vous avez déjà assez d'argent !")
            choix_continuer = input("Voulez vous terminer la manche ou continuer ?")
            if choix_continuer == "Terminer":
                tour_restant += 4
                dette_suivante = dette * 3
                dette += -dette + dette_suivante
            elif choix_continuer == "Continuer":
                continue
        elif dette <= deposer:
            tour_restant += 4
            dette_suivante = dette * 3
            dette += -dette + dette_suivante
                 

        

        
if __name__ == "__main__":
    jeu()