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

temp1 = Temperature(-273.16)
temp2 = Temperature(2)
print(temp2.celsius)
temp2.celsius = -273.12
temp1 = Temperature.fromfahrenheit(32)
print(temp1.celsius)