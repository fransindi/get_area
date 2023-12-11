class Shape:
    def __init__(self,side1, side2):
        self.side1 = side1
        self.side2 = side2
    def get_area(self):
        return self.side1 * self.side2
    def __str__(self):
        return f"The area of this {self.__class__.__name__} is: {self.get_area()}"
    
class Rectangle(Shape):
    pass

class Square(Shape):
    def __init__(self, side):
        super().__init__(side, side)

class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def get_area(self):
        area = super().get_area()
        return area / 2

from math import pi

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * (self.radius ** 2)
    
from math import sqrt

class Hexagon(Rectangle):
    def get_area(self):
        return (3 * sqrt(3) * self.side1 ** 2) / 2

class Run():
    def __init__(self):
        pass

    def jugar(self):
        print('Ingresa la forma que quieres usar\n1 para el cuadrado\n2 para el rectangulo\n3 para el circulo\n4 para el hexagono')
        forma = input()
        if forma == '1':
            print("ingresa la longitud del lado -->")
            side1 = int(input())
            cuadrado = Square(side1)
            print(f'El area de tu cuadrado es de {cuadrado.get_area()}')
        elif forma == '2':
            print('Ingresa la base -->')
            side1 = int(input())
            print("Ingresa la altura -->")
            side2 = int(input())
            rectangulo = Rectangle(side1, side2)
            print(f'El area de tu rectangulo es de {rectangulo.get_area()}')
        elif forma == '3':
            print("Ingresa el radio -->")
            radius = int(input())
            circulo = Circle(radius)
            print(f'El area de tu circulo es de {circulo.get_area()}')
        elif forma == '4':
            print('Ingresa la base -->')
            side1 = int(input())
            print('Ingresa la altura -->')
            side2 = int(input())
            hexagono = Hexagon(side1, side2)
            print(f'El area de tu hexagono es de {hexagono.get_area()}')
        else:
            print("Ingresa un numero valido.")


        


a = Run()

a.jugar()
