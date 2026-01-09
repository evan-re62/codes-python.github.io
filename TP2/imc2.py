poid = int(input("Veuiilez svp entrrer votre poids en kg : "))
taille = float(input("Veuillez svp entrer votre taille en m : "))
imc = round(float(poid)/float(taille)**2, 2)
Situation = ""

if imc < 18.5:
    Situation = "Vous êtes dans une situation de maigreur"
elif 18.5 <= imc < 25:
    Situation = "Vous êtes en situation de poids normal"
elif 25 <= imc < 30:
    Situation = "Vous êtes en surpoids"
elif 30 <= imc:
    Situation = "Vous êtes en situation d'obésité"
print("Votre IMC est de", imc,".", Situation)
    
