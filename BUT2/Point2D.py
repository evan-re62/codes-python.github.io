import math
class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance (self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    def deplace (self, dx, dy):
        self.x =+ dx
        self.y =+ dy
    def __repr__(self):
        return f"Point2D({self.x},{self.y})"



p1 = Point2D(1,2)
p2 = Point2D(4,6)

print(p1)
print(p2)


dist1 = p1.distance(p2)
print(dist1)

p1.deplace(1, -1)
print(p1)
