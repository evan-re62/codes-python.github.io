import math

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def celsius (self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Sous le zéro absolue")
        self._celsius = value
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @classmethod
    def fromfahrenheit(cls, value):
        return cls((value - 32) * 5/9)
      
    @property
    def kelvin(self):
        return self._celsius + 273.15

# --- Tests à valider ---
t = Temperature(20)
assert t.celsius == 20
assert t.fahrenheit == 68
assert t.kelvin == 293.15

t.celsius = -10
assert t.celsius == -10
assert t.kelvin == 263.15

# Test de la validation
try:
    t_invalide = Temperature(-300)
except ValueError as e:
    print(f"Exception attrapée avec succès : {e}")

try:
    t.celsius = -400
except ValueError as e:
    print(f"Exception attrapée avec succès : {e}")

print("Tests de l'exercice 3 passés avec succès !")