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

heure1 = Heure.fromsecond(15000)
heure2 = Heure(4, 10, 0)
print(heure1)
print(heure2)
print(heure1 == heure2)

            


