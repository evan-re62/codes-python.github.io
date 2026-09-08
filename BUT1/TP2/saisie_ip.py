IP = input("Veuillez enter une adresse ipv4")
Validité = 0
chiffre = 0
Liste = IP.split(".")


if len(Liste) == 4:
    for i in range(len(Liste)):
        chiffre = Liste[i]
        if int(chiffre) >= 0 and int(chiffre) <= 255:
            Validité += 1
        else:
            Validité += 0
else:
    print(IP, "n'est pas une adresse Ipv4 valide")


if Validité == 0:
    None
if Validité == 4:
    print(IP, "est une adresse IPv4 valide")
elif 0 < Validité < 4:
    print(IP, "n'est pas une adresse Ipv4 valide")