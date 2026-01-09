poid = int(input("Veuiilez svp entrrer votre poids en kg : "))
taille = float(input("Veuillez svp entrer votre taille en m : "))
IMC = round(float(poid)/float(taille)**2, 2)
print("Votre IMC est de : ", IMC)