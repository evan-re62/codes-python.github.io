import random

print("Les règles sont simples !\nTrois chiffres égaux tu double ta mise\nDeux chiffres égaux tu multiplie ta mise part 1,5\nAucun chiffres égaux tu perd tout :)")
mise = int(input("Combiens mise-tu d'argent ? "))
mise_départ = mise 
jeu = 1
while jeu == 1:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    print(f"Les chifres tombés sont : {a} {b} {c}")
    if a == b == c:
        mise = mise*2
        print(f"Tu as doublé ta mise ! Elle est dorénavant à {mise}")
        jeu = int(input("Veut tu continuer à jouer\nMet 1 pour continuer\nMet 0 pour arrêter\nTon choix : "))
    elif a == b or a == c or b == c:
        mise = mise*1.5
        print(f"Tu as multiplié ta mise part 1.5 ! Elle est dorénavant à {mise}")
        jeu = int(input("Veut tu continuer à jouer\nMet 1 pour continuer\nMet 0 pour arrêter\nTon choix : "))
    else:
        if mise != mise_départ:
            print(f"Tu as tout perdu ! Quel dommage, tu avais réussi à atteindre {mise}$")
            break
        elif mise == mise_départ:
            print(f"Pas de chance, tu as tout perdu directement.. :(")
            break

argent_gagner = mise - mise_départ   

if jeu == 0:
    print(f"Félicitations tu as gagner de l'argent ! Ta mise finale est de {mise}$ ! Tu as donc gagner en tout {argent_gagner}$ !  ")



