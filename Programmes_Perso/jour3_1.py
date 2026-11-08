

solde = 500

while True:
    print("""===== BANQUE =====
    1. Voir mon solde
    2. Déposer de l'argent
    3. Retirer de l'argent
    4. Quitter""")
    action = int(input("Que voulez-vous faire ? "))
    if action == 1:
        print(f"Votre solde est de {solde}$")
    elif action == 2:
        verif = solde
        solde += int(input("Combiens d'argent voulez vous ajouter ? "))
        if verif >= solde:
            print("Veuillez mettre un nombre positif.")
            solde = verif
        else:
            print(f"L'argent à bien été ajouter au compte")
    elif action == 3:
        verif = solde
        solde += -int(input("Combiens voulez vous retirer ? "))
        if verif <= solde:
            print("Veuillez indiquer un nombre positif")
            solde = verif
        elif solde < 0:
            print("Sa serais bête de s'endetter")
            solde = verif          
        else:
            print("L'argent à bien été retirer du compte.")
    elif action == 4:
        break

