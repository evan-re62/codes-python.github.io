import random


SYMBOLES = ["Citron", "Cerise", "Trèfle", "Cloche", "Diamant", "Coffre", "7"]

VALEURS_SYMBOLES = {"Citron": 2, "Cerise": 2, "Trèfle": 3,
                     "Cloche": 3, "Diamant": 5, "Coffre": 5, "7": 7 }

MULTIPLICATEURS_FORME = {"Hor": 1, "Vert": 1, "Diag": 1, "Hor-L": 2, "Hor-XL": 3, 
                         "Zig": 4, "Zag": 4, "Above": 7, "Below": 7, "Eye": 8, "JACKPOT": 10} 



def calculer_gain(liste):
    