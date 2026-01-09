import random
devine = random.randint(0, 100)
nombre = 0
tentatives = 0
while nombre != devine:
    nombre = int(input("Donne un nombre "))
    tentatives += 1
    if nombre > devine:
        print("Plus petit")
    else:
        print("Plus grand")
print("Bien joué, vous avez fait", tentatives, "tentatives.")
