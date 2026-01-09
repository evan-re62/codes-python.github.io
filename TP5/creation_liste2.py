import random

def liste_utilisateur(n):
    liste = []
    for i in range(n):
        liste.append(input("Un nombre "))
    return liste

def liste_random(n=5, bornemin=0, bornemax=100):
    liste = []
    for i in range(5):
        liste.append(random.randint(bornemin, bornemax))
    return liste

if __name__ == "__main__":
    l1=liste_utilisateur(4)
    print(l1)
    l2=liste_random(4)
    print(l2)