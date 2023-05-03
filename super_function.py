# Super() = function is used to give access to the methods of a parent class.
#           It returns a temporary object of a parent class when used.

class Rectangle:
    pass

class Square(Rectangle):

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height


square = Square(3, 3)

cube = Cube(3, 3, 3)

# By observing the Square and Cube methods, they use the same properties
# therefore we can define this in the parent class and use the Super() 
# method to class to call this from the children

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(3, 3)

cube = Cube(3, 3, 3)

print(square.area())

print(cube.volume())