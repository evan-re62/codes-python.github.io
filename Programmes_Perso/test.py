import random


SYMBOLES = ["🍋", "🍒", "🍀", "🔔", "💎", "📦", "⭐"]

POURCENTAGE = [19.4, 19.4, 14.9, 14.9, 11.9, 11.9, 7.6]

CHANCE_OR = {"🍋": 5, "🍒": 0, "🍀": 0,
                    "🔔": 20, "💎": 0, "📦": 5, "⭐": 10}

VALEURS_SYMBOLES = {"🍋": 2, "🍒": 2, "🍀": 3,
                    "🔔": 3, "💎": 5, "📦": 5, "⭐": 7}

LUCK = 0
liste = []

if LUCK > 0:
        symbole_forcé = SYMBOLES[random.randint(0, 6)]
        for i in range(LUCK):
            etat = "Gold" if random.randint(1, 100) <= CHANCE_OR[symbole_forcé] else "Normal"
            liste.append({symbole_forcé: etat })

for i in range(15 - LUCK):
    symbole = SYMBOLES[random.randint(0, 6)]
    etat = "Gold" if random.randint(1, 100) <= CHANCE_OR[symbole] else "Normal"
    liste.append({symbole: etat })


random.shuffle(liste)
grille = [liste[i * 5:(i + 1) * 5] for i in range(3)]


for ligne in grille:
    cases = []
    for case in ligne:
        symbole, etat = list(case.items())[0]
        if etat == "Gold":
            texte = f"{symbole}🪙"
            cases.append(f"{texte:<5}")
        else:
            texte = symbole
            cases.append(f"{texte:<5}")
    print("")
    print("  ".join(cases))