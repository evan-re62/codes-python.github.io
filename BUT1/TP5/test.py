import random

def adresses_ip(classe:str="A") -> str:
    adresse = ""
    if classe == "A":
        adresse += str(random.randint(0, 127))
        for i in range(3):
            adresse += "."
            adresse += str(random.randint(0, 255))
            
            print(adresse)
    return adresse
print(adresses_ip("A"))