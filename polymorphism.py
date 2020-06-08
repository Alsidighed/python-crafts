from math import *

class Shape:
    def __init__(self, type):
        self.type = type
    def __str__(self):
        return f"{self.type}, {self.properties()}, площадь = {self.square()}, периметр = {self.perimeter()}"
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        type = "Прямоугольник"
        if width == height:
            type = "Квадрат"
        super().__init__(type)
    def properties(self):
        return f"длина = {self.height}, ширина = {self.width}"
    def square(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def properties(self):
        return f"сторона = {self.width}"
    def square(self):
        return self.width * self.width
    def perimeter(self):
        return 4 * self.width
class Triangle(Shape):
    def __init__(self, width, height, leftToHeight):
        self.width = width
        self.height = height
        self.leftToHeight = leftToHeight
        super().__init__("Треугольник")
    def properties(self):
        return f"основание = {self.width}, высота = {self.height}, расстояние до высоты с левого края основания = {self.leftToHeight}"
    def square(self):
        return self.width * self.height / 2
    def getSides(self):
        if self.leftToHeight == 0: # Прямоугольный, угол слева
            return self.height, sqrt(self.height ** 2 + self.width ** 2)
        if self.leftToHeight == self.width: # Прямоугольный, угол справа
            return sqrt(self.height ** 2 + self.width ** 2), self.height
        if self.leftToHeight < 0: # Высота опущена левее основания
            return sqrt(self.height ** 2 + self.leftToHeight ** 2), sqrt(self.height ** 2 + (self.width + self.leftToHeight) ** 2)
        if self.leftToHeight > self.width: # Высота опущена правее основания
            return sqrt(self.height ** 2 + (self.width + self.leftToHeight) ** 2), sqrt(self.height ** 2 + self.leftToHeight ** 2)
        return sqrt(self.height ** 2 + self.leftToHeight ** 2), sqrt(self.height ** 2 + (self.width - self.leftToHeight) ** 2) # Высота опущена на основание
    def perimeter(self):
        return self.width + sum(self.getSides())
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__("Круг")
    def properties(self):
        return f"радиус = {self.radius}"
    def square(self):
        return pi * self.radius ** 2
    def perimeter(self):
        return 2 * pi * self.radius
        
print(Rectangle(5, 10))
print(Square(6))
print(Triangle(11, 4, 8))
print(Circle(16))
