liste = [2, 3, 5, 7]

choix = input("Souhaitez vous ajouter ou supprimer un entier ? (a/s) ")
indice = int(input("A quel indice ?"))

if choix == "a":
    entier = int(input("Quel entier ? "))
    liste.insert(indice, entier)
    print(liste)
elif choix == "s":
    del(liste[indice])
    print(liste)

