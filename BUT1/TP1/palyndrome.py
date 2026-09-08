mot = input("Donne un mot stp : ")
if mot == mot[::-1]:
    print(mot, "est un palyndrome")
else:
    print(mot, "n'est pas un palyndrome")
