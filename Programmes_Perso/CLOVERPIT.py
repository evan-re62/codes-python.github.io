import random


SYMBOLES = ["🍋", "🍒", "🍀", "🔔", "💎", "📦", "⭐"]

POURCENTAGE = [19.4, 19.4, 14.9, 14.9, 11.9, 11.9, 7.5]

VALEURS_SYMBOLES = {"🍋": 2, "🍒": 2, "🍀": 3,
                    "🔔": 3, "💎": 5, "📦": 5, "⭐": 7}

MULTIPLICATEURS_FORME = {"Hor": 1, "Vert": 1, "Diag": 1, "Hor-L": 2, "Hor-XL": 3, 
                         "Zig": 4, "Zag": 4, "Above": 7, "Below": 7, "Eye": 8, "JACKPOT": 10} 

grille = [[random.choices(SYMBOLES, weights=POURCENTAGE, k=1)[0] for _ in range(5)] for _ in range(3)]

for ligne in grille:
    print(*ligne)
    

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
            gain += VALEURS_SYMBOLES[ligne[i]] * 3 * MULTIPLICATEURS_FORME["Vert"]
    for i in range(3):
        if grille[0][i] == grille[1][i+1] == grille[2][i+2]:
            gain += VALEURS_SYMBOLES[ligne[i]] * 3 * MULTIPLICATEURS_FORME["Diag"]
    for i in range(3):
            if grille[2][i] == grille[1][i+1] == grille[0][i+2]:
                gain += VALEURS_SYMBOLES[ligne[i]] * 3 * MULTIPLICATEURS_FORME["Diag"]

    if grille[0][2] == grille[1][1] == grille[1][3] == grille[2][0] == grille[2][4]:
        gain += VALEURS_SYMBOLES[ligne[i]] * 5 * MULTIPLICATEURS_FORME["Zig"]

    if grille[0][0] == grille[0][4] == grille[1][1] == grille[1][3] == grille[2][2]:
            gain += VALEURS_SYMBOLES[grille[0][0]] * 5 * MULTIPLICATEURS_FORME["Zag"]
    if grille[0][2] == grille[1][1] == grille[1][3] == grille[2][0] == grille[2][1] == grille[2][2] == grille[2][3] == grille[2][4]:
         gain += VALEURS_SYMBOLES[grille[0][2]] * 8 * MULTIPLICATEURS_FORME["Above"]
    if grille[0][0] == grille[0][1] == grille[0][2] == grille[0][3] == grille[0][4] == grille[1][1] == grille[1][3] == grille[2][2]:
         gain += VALEURS_SYMBOLES[grille[0][0]] * 8 * MULTIPLICATEURS_FORME["Below"]
    if grille[0][1] == grille[0][2] == grille[0][3] == grille[1][0] == grille[1][1] == grille[1][3] == grille[1][4] == grille[2][1] == grille[2][2] == grille[2][3]:
         gain += VALEURS_SYMBOLES[grille[0][1]] * 10 * MULTIPLICATEURS_FORME["Eye"]
    for ligne in grille:
        if ligne[0] == ligne[1] == ligne[2]:
            gain += VALEURS_SYMBOLES[ligne[i]] * 15 * MULTIPLICATEURS_FORME["JACKPOT"]
            
    return gain




if __name__ == "__main__":
    print(calculer_gain(grille))