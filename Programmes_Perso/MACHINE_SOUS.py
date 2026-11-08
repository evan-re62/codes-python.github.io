import random
import time

SYMBOLES = ["Cerise", "Citron", "Trèfle", "Cloche", "Diamant", "Coffre", "7"]

Solde = 1000

Mise = 10

Continuer = True

def calculer_gain(liste, Solde, Mise):
    Solde -= Mise
    Gain = 0
    if liste[0] == liste[1] == liste[2]:
        if liste[0] == SYMBOLES[0]:
            Gain = Mise*5
        if liste[0] == SYMBOLES[1] or liste[0] == SYMBOLES[2] or liste[0] == SYMBOLES[3]:
            Gain = Mise*15
        if liste[0] == SYMBOLES[4]:
            Gain = Mise*20
        if liste[0] == SYMBOLES[5]:
            Gain = Mise*100
        if liste[0] == SYMBOLES[6]:
            Gain = Mise*250
    if liste[0] == SYMBOLES[0] and liste[1] == SYMBOLES[0] or liste[1] == SYMBOLES[0] and liste[2] == SYMBOLES[0]:
        Gain = Mise*2
    Solde += Gain

    return Solde, Gain

def roulette():
    roue = [SYMBOLES[random.randint(0, 6)] for i in range(3)]
    return roue

while Continuer:
    if Solde <= 0:
        print("Vous n'avez plus d'argent.")
        break
    Encore = input("\nVoulez vous continuer ? ")
    if Encore == "Oui" :
        print(f"\nVotre solde : {Solde}")
        while True:
            Mise = int(input("\nVeuillez entrer votre mise : "))
            if Mise <= Solde:
                break
            else:
                print("\nLa mise ne doit pas dépasser le solde.")
        roue = roulette()
        print(f"Résultat de la roulette : {roue}")
        Solde_Pre = Solde
        Solde, Gain = calculer_gain(roue, Solde, Mise)
        time.sleep(1.5)
        if Solde_Pre > Solde:
            print(f"\nVous n'avez rien gagner. Votre solde est maintenant égal à {Solde}.")
        else:
            print(f"\nVous avez gagner un gain de {Gain}$ ! Votre solde est maintenant égal à {Solde}$ ! ")
    elif Encore == "Non":
        Continuer = False

    else:
        print("\nVeuillez entrer Oui ou Non")
