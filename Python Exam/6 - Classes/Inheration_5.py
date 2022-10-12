'''
1 - Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:
2 - Define a Area() method of the class which calculates the area of ​​the circle.
3 - Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
4 - Define a testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not.
'''

from math import pi

class Circle:
    def __init__(self,a,b,r):
        #self.center=(a,b)
        self.a=a
        self.b=b
        self.r= r
    def area(self):
        return f"Circle area equals :{pi * self.r ** 2}"

    def perimetr(self):
        return f" Circle perimetr is :{2 * pi * self.r}"


    def test_belongs(self, x, y):
        if (x - self.a) ** 2 + (y - self.b) ** 2 == self.r ** 2:
            return f"Coordination {x, y} belongs to circle"
        else:
            return f"Coordination {x, y} don't belongs to circle"


if __name__ == '__main__':
    my_circle= Circle(1, 2, 1)
    print(my_circle.area())
    print(my_circle.perimetr())
    print(my_circle.test_belongs(1,1))
