import math
class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance (self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    def deplacer (self, dx, dy):
        self.x += dx
        self.y += dy
    def __repr__(self):
        return f"Point2D({self.x},{self.y})"


# --- Tests à valider ---
p1 = Point2D(1, 2)
p2 = Point2D(4, 6)

print(f"Point 1 : {p1}")
print(f"Point 2 : {p2}")

# Test de la distance
dist = p1.distance(p2)
print(f"Distance entre p1 et p2 : {dist}")
assert math.isclose(dist, 5.0), "La distance devrait être 5.0"

# Test du déplacement
p1.deplacer(1, -1)
print(f"Point 1 après déplacement : {p1}")
assert p1.x == 2 and p1.y == 1, "Le point devrait être à (2, 1)"

print("Tests de l'exercice 1 passés avec succès !")