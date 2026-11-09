class Heure:
    def __init__(self, h, m, s):
        if 0 <= h <= 23:
            self.h = h
        else:
            raise ValueError("Non")

        if 0 <= m <= 59:
            self.m = m
        else:
            raise ValueError("Non")

        if 0 <= s <= 59:
            self.s = s
        else:
            raise ValueError("Non")
    @classmethod
    def fromsecond(cls, total_secondes: int):
        heure, reste_m = divmod(total_secondes, 3600)
        minutes, reste_s = divmod(reste_m,60)
        secondes = reste_s
        return cls(heure,minutes,secondes)
    def __repr__(self):
        return f"Heure({self.h}, {self.m}, {self.s})"
    def __str__(self):
        return f"Il est actuellement {self.h}:{self.m}:{self.s}"
    def __eq__(self, other):
        return self.h == other.h and self.m == other.m and self.s == other.s

h1 = Heure(1, 1, 1)
print(f"repr(h1): {repr(h1)}")
print(f"str(h1): {str(h1)}")

# Test du classmethod
total_secs = 3661 # 1 heure, 1 minute, 1 seconde
h2 = Heure.fromsecond(total_secs)
assert h2.h == 1 and h2.m == 1 and h2.s == 1

# Test de l'égalité
h3 = Heure(1, 1, 1)
assert h1 == h2
assert h1 == h3
assert h2 != Heure(1, 1, 2)

print("Tests de l'exercice 4 passés avec succès !")


