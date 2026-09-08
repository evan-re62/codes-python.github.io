from collections import Counter 
liste_suspect = []
stop = 0
while stop == 0:
    liste_suspect.append(input("Entre un nom stp : "))
    stop = int(input("0 pour continuer\nAutre pour arrêter\nVotre choix : "))
dict = dict(Counter((liste_suspect)))

suspect = max(dict, key=dict.get)
print(f"Voicis les différents suspects potentiels et leurs nombres de mentions : {dict}\nEt le mec le plus suspecté est : {suspect}")