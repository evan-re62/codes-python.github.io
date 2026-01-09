liste = []
while True:
    entier = 0
    entier = input("Entier (""stop"" pour finir) : ")
    if entier == "stop":
        break
    else:
        liste.append(int(entier))
print(liste)