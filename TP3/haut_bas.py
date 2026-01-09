
h_b = input("Voulez-vous compter vers le haut (h) ou vers le bas (b) ? ")
n = int(input("n ?(plus petit que 50) "))

if n > 50:
    print("Je ne comprends pas votre choix.")
elif h_b == "h":
    for i in range(0, n+1):
        print(i, end=", ")
elif h_b == "b":
    for i in range(50, n-1, -1):
        print(i, end=", ")

        
