code_coffre = "8395"
nombre_tent = 0
tent = 0
while nombre_tent < 3:
    tent = input("Quel est le code ? ")
    nombre_tent += 1
    if tent == code_coffre:
        print("Bravo ! Tu as craquer le code du coffre")
        break
    else:
        print(f"IL te reste {3 - nombre_tent} tentatives !")
    if nombre_tent == 3:
        print("Quel dommage, le coffre c'est vérouiller et la police à été prévenue. Bon séjour en prison ! ")

