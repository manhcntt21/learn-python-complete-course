# super(): function used to give access to the methods of a parent class
# returns a temporary object of a parent class when used

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


if __name__ == '__main__':
    square = Square(2, 2)
    cube = Cube(2, 2, 2)
    print(square.area(), cube.volume())

    print(type(square))
    print(type(cube))