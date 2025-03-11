class Shape:
    def area(self):
        pass 
    def circumference(self):
        pass
    
class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height 

    def circumference(self):
        return 2 * (self.__width + self.__height) 

class Circle(Shape):

    def __init__(self, radius): 
        self.__pi = 3.1416
        self.__radius = radius
    
    def area(self): 
        return self.__pi * self.__radius**2

    def circumference(self):
        return 2 * self.__pi * self.__radius 
