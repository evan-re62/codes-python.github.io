mot = input("Mot ? ")
nombre = int(input("Nombre de répétition ? "))
chaine_mot = " "
for i in range(nombre):
    chaine_mot += mot+" "
print("Voici", nombre, "répétitions :",chaine_mot)

