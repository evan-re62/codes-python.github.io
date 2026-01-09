n = int(input("n ? (inférieur à 20) "))

if n >= 20:
    print("Choisis un nombre inférieur à 20")
else:
    for i in range(20,n-1, -1):
        print(i, end=",")