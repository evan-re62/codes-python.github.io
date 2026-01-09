adresse_ip = input("Adresse IP ? ")
premier_octet = ""
liste = list(adresse_ip)
for i in range(len(liste)):
    premier_octet += liste[i]

verif = premier_octet.split(".")

if  0 <= int(verif[0]) <= 127:
    print("L'adresse", premier_octet, "est de classe A")
elif  128 <= int(verif[0]) <= 191:
    print("L'adresse", premier_octet, "est de classe B")
elif 192 <= int(verif[0]) <= 223:
    print("L'adresse", premier_octet, "est de classe C")
elif  224 <= int(verif[0]) <= 239:
    print("L'adresse", premier_octet, "est de classe D")
elif  int(verif[0]) > 240:
    print("L'adresse", premier_octet, "est de classe E")


