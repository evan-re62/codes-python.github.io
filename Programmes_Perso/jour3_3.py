import random
score = 0
choix = 2
while True:
    face = random.randint(1,6)
    if face == 1:
        score += -10
    if face == 2 or face == 3:
        score += 5
    if face == 4 or face == 5:
        score += 10
    if face == 6:
        score += 25
    print(f"Vous avez fais {face} donc votre score actuel est de {score}")
    while choix != 1 and choix != 0:
        choix = int(input("1 Pour continuer\n0 Pour arrêter\n "))
        print(choix)
    if choix == 0:
        break
    choix = 2

    
    