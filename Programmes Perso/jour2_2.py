inventaire = ["épée","potion","bouclier"]

print(""" ===== INVENTAIRE =====
1. Voir l'inventaire
2. Ajouter un objet
3. Supprimer un objet
4. Chercher un objet
5. Quitter""")
while True:

    choix = int(input("Que voulez vous faire ? "))
    if choix == 1:
        print(inventaire)
    if choix == 2:
        inventaire.append(input("Quel objet : "))
    if choix == 3:
        inventaire.remove(input("Quel objet veut-tu supprimmer ? " ))
    if choix == 4:
        cherche = input("Quel objet veut-tu chercher ? ")
        if cherche not in inventaire:
                        print("Tu n'a pas cet objet dans ton inventaire")
        for objet in inventaire:
            if cherche == objet:
                print(f"Tu dispose bien de cet objet : {cherche}")
    if choix == 5:
        break