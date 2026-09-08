import random

def adresses_ip(classe:str="A") -> str:
    adresseip = ""
    if classe == "A":
        adresseip += str(random.randint(0, 127))
        for i in range(3):
            adresseip += "."
            adresseip += str(random.randint(0, 255))
    if classe == "B":
        adresseip += str(random.randint(128, 191))
        for i in range(3):
            adresseip += "."
            adresseip += str(random.randint(0, 255))
    if classe == "C":
        adresseip += str(random.randint(192, 223))
        for i in range(3):
            adresseip += "."
            adresseip += str(random.randint(0, 255))
    if classe == "D":
        adresseip += str(random.randint(224, 239))
        for i in range(3):
            adresseip += "."
            adresseip += str(random.randint(0, 255))
    if classe == "E":
        adresseip += str(random.randint(240, 255))
        for i in range(3):
            adresseip += "."
            adresseip += str(random.randint(0, 255))
    return adresseip

def classe(adresse):
    octet = []
    octet += adresse.split(".")
    if 0 <= int(octet[0]) <= 127:
        classe = "A"
    if 128 <= int(octet[0]) <= 191:
        classe = "B"
    if 192 <= int(octet[0]) <= 223:
        classe = "C"
    if 224 <= int(octet[0]) <= 239:
        classe = "D"
    if 240 <= int(octet[0]) <= 255:
        classe = "E"
    return classe




if __name__ == "__main__":
    adr = adresses_ip("E")
    print(f"{adr} est de classe {classe(adr)}")

