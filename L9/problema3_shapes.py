import math  # Importăm modulul math pentru valoarea lui pi


# Clasa de bază Shape
# Aceasta definește o formă geometrică generală
class Shape:

    # Metodă care va fi suprascrisă în clasele copil
    def area(self):
        return 0


# Clasa Circle moștenește Shape
class Circle(Shape):

    # Constructorul clasei Circle
    def __init__(self, radius):
        self.radius = radius  # raza cercului

    # Calculăm aria cercului
    def area(self):
        return math.pi * self.radius ** 2

    # Metodă dunder pentru afișarea obiectului
    def __str__(self):
        return f"Circle with radius {self.radius} has area {self.area():.2f}"


# Clasa Rectangle moștenește Shape
class Rectangle(Shape):

    # Constructorul clasei Rectangle
    def __init__(self, width, height):
        self.width = width  # lățimea dreptunghiului
        self.height = height  # înălțimea dreptunghiului

    # Calculăm aria dreptunghiului
    def area(self):
        return self.width * self.height

    # Metodă dunder pentru afișarea obiectului
    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area()}"


# Creăm obiecte pentru fiecare formă
circle = Circle(5)
rectangle = Rectangle(10, 4)

# Afișăm obiectele (se apelează automat __str__)
print(circle)
print(rectangle)
