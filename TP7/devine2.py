import random
devine = random.randint(0, 100)
nombre = 0
tentatives = 0
while tentatives < 10:
    nombre = int(input("Donne un nombre "))
    tentatives += 1
    print(tentatives)
    if nombre > devine:
        print("Plus petit")
    elif nombre < devine:
        print("Plus grand")
    elif nombre == devine:
        print("Bien joué, vous avez fait", tentatives, "tentatives.")
        break

if tentatives == 10:
    print("Ah zut perdu, vous avez atteint le nombre maximum de tentatives, le nombre cherché était", devine)
