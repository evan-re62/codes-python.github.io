import random

# 1. Générer la grille : 3 lignes de 5 éléments (chiffres entre 0 et 9)
grille = [[random.randint(0, 9) for _ in range(5)] for _ in range(3)]

# Afficher la grille pour voir ce qui est généré
print("Grille générée :")
for ligne in grille:
    print(ligne)

points = 0

# 2. Vérification HORIZONTALE (lignes de 3 consécutifs)
for ligne in grille:
    for i in range(3):
        if ligne[i] == ligne[i+1] == ligne[i+2]:
            points += 1

# 3. Vérification des DIAGONALES (longueur 3)
# Comme la grille fait 3 lignes, les diagonales font exactement 3 de long.
# Il y a 3 positions de colonnes possibles pour commencer une diagonale (0, 1 ou 2).

# Diagonales descendantes (\)
for c in range(3):
    if grille[0][c] == grille[1][c+1] == grille[2][c+2]:
        points += 1

# Diagonales montantes (/)
for c in range(3):
    if grille[2][c] == grille[1][c+1] == grille[0][c+2]:
        points += 1

print(f"\nTotal des points gagnés : {points}")