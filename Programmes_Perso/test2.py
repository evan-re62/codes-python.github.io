import random


SYMBOLES = ["🍋", "🍒", "🍀", "🔔", "💎", "📦", "⭐"]

POURCENTAGE = [19.4, 19.4, 14.9, 14.9, 11.9, 11.9, 7.5]

VALEURS_SYMBOLES = {"🍋": 2, "🍒": 2, "🍀": 3,
                    "🔔": 3, "💎": 5, "📦": 5, "⭐": 7}

MULTIPLICATEURS_FORME = {"Hor": 1, "Vert": 1, "Diag": 1, "Hor-L": 2, "Hor-XL": 3, 
                         "Zig": 4, "Zag": 4, "Above": 7, "Below": 7, "Eye": 8, "JACKPOT": 10}

def telephone():
    Choix1 = ""
    Choix2 = ""
    Choix3 = ""
    for i in range(3):
        n = random.randint(1, 3)
        if n == 1:
            symb_spawn = random.randint(0,6)
            spawn = POURCENTAGE[symb_spawn]
            augm_spawn = random.randint(2,5)
            if i == 0:
                Choix1 = print(f"\nChoix : \nAugmenter le taux d'apparitions de {SYMBOLES[symb_spawn]} de {augm_spawn}%")
            elif i == 1:
                Choix2 = print(f"\nAugmenter le taux d'apparitions de {SYMBOLES[symb_spawn]} de {augm_spawn}%")
            elif i == 2:
                Choix3 = print(f"\nAugmenter le taux d'apparitions de {SYMBOLES[symb_spawn]} de {augm_spawn}%")
        if n == 2:
            val_symb = SYMBOLES[random.randint(0, 6)]
            val = VALEURS_SYMBOLES[val_symb]
            augm_val_symb = random.randint(1, 3)
            if i == 0:
                Choix1 = print(f"\nChoix : \nAugmenter la valeur de {val_symb} de {augm_val_symb}$")
            elif i == 1:
                Choix2 = print(f"\nAugmenter la valeur de {val_symb} de {augm_val_symb}$")
            elif i == 2:
                Choix3 = print(f"\nAugmenter la valeur de {val_symb} de {augm_val_symb}$")

        if n == 3:
            nom = list(MULTIPLICATEURS_FORME)
            forme = nom[random.randint(0, 10)]
            augm_multi_forme = random.randint(1, 2)
            if i == 0:
                Choix1 = print(f"\nChoix : \nAugmenter la valeur de {forme} de {augm_multi_forme}")
            elif i == 1:
                Choix2 = print(f"\nAugmenter la valeur de {forme} de {augm_multi_forme}")
            elif i == 2:
                Choix3 = print(f"\nAugmenter la valeur de {forme} de {augm_multi_forme}")














telephone()