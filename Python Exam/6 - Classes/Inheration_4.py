'''
Write a Rectangle class, allowing you to build a rectangle with length and width attributes.
- Create a perimeter() method to calculate the perimeter of the rectangle and an area() method to
calculate the area of the rectangle and diagonal() method
- Create a method display() that display the length, width, perimeter and area of an object created
using an instantiation on rectangle class.
- Create a Cuboid child class inheriting from the Rectangle class and with a height attribute and
another volume() method to calculate the volume of the Cuboid.
'''


import math
class Rectangule:
    def __init__(self, lenght, width):
        self.lenght=lenght
        self.width=width

    def perimeter(self):
        return 2*(self.lenght+self.width)
    def area(self):
        return self.lenght*self.width
    def diagonal(self):
        return math.ceil(math.sqrt(self.lenght**2+self.width**2))

    @property
    def display(self):
        return f" Lenght: {self.lenght}, width:{self.width}, perimeter :{self.perimeter()}, area:{self.area()}, diagonal:{self.diagonal()}"


class Cuboid(Rectangule):
    def __init__(self, lenght, weight, height):
        super().__init__(lenght, weight)
        self.height= height
    @property
    def  volume(self):
        return self.area()*self.height


if __name__ == '__main__':
    rect= Rectangule(3,4)
    print(rect.perimeter())
    print(rect.display)
    d=Cuboid(3,4,5)
    print(d.volume)


