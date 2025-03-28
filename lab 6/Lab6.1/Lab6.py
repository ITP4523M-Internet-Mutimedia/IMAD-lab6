class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height 

    def circumference(self):
        return 2 * (self.__width + self.__height) 
    