def carre_blanc(n:int=8) -> None:
    print("* "*n)
    for i in range(n-2):
        print("* "+" "*(n-2)*2+"*")
    print("* "*n)  

def carre(n:int=8) -> None:
    for i in range(n):
        print("* "*n)

def tri_rect(h:int=8) -> None:
    for i in range(h+1):
        print("*"*i)


def tri_iso(h:int=8) -> None:
    for i in range(h):
        print(" "*(h-1-i) + "*"*(1+2*i))
    


if __name__ == "__main__":
    carre()
    print()
    carre_blanc()
    print()
    tri_rect()
    print()
    tri_iso()