niveau = 1
xp = 0

while True:
    while xp >= 100:
        niveau += 1
        xp = xp - 100
    print(f"""===== JOUEUR =====
    Niveau : {niveau}
    XP : {xp}
    1. Faire une quête (+50 XP)
    2. Tuer un boss (+150 XP)
    3. Voir mes statistiques
    4. Quitter""")
    action = int(input("Que voulez-vous faire ? "))
    if action == 1:
        xp += 50
        print(f"Vous avez gagner 5P d'XP !")
    if action == 2:
        xp += 150
        print(f"Vous avez gagner 150 d'XP !")
    if action == 3:
        print(f"Vous êtes actuellement au niveau {niveau} ! ")
    if action == 4:
        break

    