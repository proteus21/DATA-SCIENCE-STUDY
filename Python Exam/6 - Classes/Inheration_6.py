'''
 Write a Geometry class with default constructor having no parameters.
- Write a method in Geometry class called distance() that allow to compute a distance between two
points A = (xa, ya), B = (xb, yb)
- Write a method in Geometry class called middle() allowing to determine the middle of bipoint (A,B).
- Write method called triangle_perimeter() allowing to compute the perimeter of triangle basing on
three points
- Write method called triangle_isosceles() which returns a True if the triangle is isosceles and False if
not, basing on three points
*isosceles triangle - trójkąt równoramienny
- Write method called incircle_radius() which returns a radius of circle inside a triangle with three
points
- Write method called outcircle_radius() which returns a radius of circle outside a triangle with three
points
- *Write method called in_triangle_out_circle() which returns True if a point is inside a triangle, but
outside of incircle
- *Write method called in_circle_out_triangle() which returns True if a point is inside a circle, but
outside of intriangle

'''
import math
class Geometry:

    def distance(self, x_a, y_a, x_b, y_b):
           return f"Distance  between point A = {(x_a,y_a)} and B ={(x_b,y_b)} equals {math.sqrt((x_b-x_a)**2+(y_b-y_a)**2)} "

    def middle(self, x_a, y_a, x_b, y_b):
        return f"Middle point between two points: A = {(x_a,y_a)} and B ={(x_b,y_b)} is {((x_a +x_b)/2, (y_a +y_b)/2)}"

    def triangle_perimeter(self,x_a, y_a, x_b, y_b, x_c, y_c):
        result=math.sqrt((x_b-x_a)**2+(y_b-y_a)**2)+math.sqrt((x_c-x_a)**2+(y_c-y_a)**2)+math.sqrt((x_c-x_b)**2+(y_c-y_b)**2)
        return f"Perimeter of triangle  for points A = {(x_a,y_a)},B ={(x_b,y_b)},C ={(x_c,y_c)}  is :{result}"

    def  incircle_radius_triangle_type(self,x_a, y_a, x_b, y_b, x_c, y_c):
        a=math.sqrt((x_b-x_a)**2+(y_b-y_a)**2)
        b=math.sqrt((x_c-x_a)**2+(y_c-y_a)**2)
        c=math.sqrt((x_c-x_b)**2+(y_c-y_b)**2)
        if a == b and b == c:
            print('Triangle is Equilateral.')
            return a/(2*2**0.5)
        elif a == b or b == c or a == c:
            print('Triangle is Isosceles.')
            height_h=math.sqrt(c**2-(0.5*a**2))
            return a*height_h/(a+math.sqrt(4*height_h**2+a**2))
        else:
            print('Triangle is Scalane')

    def  outcircle_radius_triangle_type(self,x_a, y_a, x_b, y_b, x_c, y_c):
        a=math.sqrt((x_b-x_a)**2+(y_b-y_a)**2)
        b=math.sqrt((x_c-x_a)**2+(y_c-y_a)**2)
        c=math.sqrt((x_c-x_b)**2+(y_c-y_b)**2)
        if a == b and b == c:
            print('Triangle is Equilateral.')
            return a/(3**0.5)
        elif a == b or b == c or a == c:
            print('Triangle is Isosceles.')
            return (a*b*c/(math.sqrt((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))))
        else:
            print('Triangle is Scalane')
            return (a * b * c / (math.sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c))))


    def is_triangle(self,x_a, y_a, x_b, y_b, x_c, y_c):
        a=math.sqrt((x_b-x_a)**2+(y_b-y_a)**2)
        b=math.sqrt((x_c-x_a)**2+(y_c-y_a)**2)
        c=math.sqrt((x_c-x_b)**2+(y_c-y_b)**2)
        if a + b >= c and b + c >= a and c + a >= b:
            return True
        else:
            return False


    def incircle_radius(self,x_a, y_a, x_b, y_b, x_c, y_c):
        self.a=math.sqrt((x_b-x_a)**2+(y_b-y_a)**2)
        self.b=math.sqrt((x_c-x_a)**2+(y_c-y_a)**2)
        self.c=math.sqrt((x_c-x_b)**2+(y_c-y_b)**2)
        if self.is_triangle(x_a, y_a, x_b, y_b, x_c, y_c)==True:
                return  f"The lenght a= {self.a}, b={self.b}, c={self.c}  and  incicle radius is {self.incircle_radius_triangle_type(x_a, y_a, x_b, y_b, x_c, y_c)} also centerpoints {self.centroid_point(x_a, y_a, x_b, y_b, x_c, y_c)}"


    def  outcircle_radius(self,x_a, y_a, x_b, y_b, x_c, y_c):
        self.a = math.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
        self.b = math.sqrt((x_c - x_a) ** 2 + (y_c - y_a) ** 2)
        self.c = math.sqrt((x_c - x_b) ** 2 + (y_c - y_b) ** 2)
        if self.is_triangle(x_a, y_a, x_b, y_b, x_c, y_c) == True:
            return f"The lenght a= {self.a}, b={self.b}, c={self.c}  and  outcicle radius is  {self.outcircle_radius_triangle_type(x_a, y_a, x_b, y_b, x_c, y_c)} also centerpoints {self.centroid_point(x_a, y_a, x_b, y_b, x_c, y_c)} "




    def calculation_area(self,x_a, y_a, x_b, y_b, x_c, y_c):

        return abs((x_a * (y_b - y_c) + x_b * (y_c- y_a)
                    + x_c * (y_a - y_b)) / 2.0)


    def isInside(self,x_a, y_a, x_b, y_b, x_c, y_c, x, y):

        A =  self.calculation_area(x_a, y_a, x_b, y_b, x_c, y_c)

        A1 =  self.calculation_area(x, y, x_b, y_b, x_c, y_c)

        A2 = self.calculation_area(x_a, y_a, x, y, x_c, y_c)

        A3 = self.calculation_area(x_a, y_a, x_b, y_b, x, y)

        # Check if sum of A1, A2 and A3
        # is same as A
        if (A == A1 + A2 + A3):
            return True
        else:
            return False
    def  centroid_point(self,x_a, y_a, x_b, y_b, x_c, y_c):
        return ((x_a+x_b+x_c)/3,(y_a+y_b+y_c)/3)

    def point_out_circle(self,x_a, y_a, x_b, y_b, x_c, y_c, x, y):
        if (x - self.centroid_point(x_a, y_a, x_b, y_b, x_c, y_c)[0]) ** 2 + (y - self.centroid_point(x_a, y_a, x_b, y_b, x_c, y_c)[1]) ** 2 == self.outcircle_radius_triangle_type(x_a, y_a, x_b, y_b, x_c, y_c) ** 2:
            return f"Coordination {x, y} belongs to circle"
        else:
            return f"Coordination {x, y} don't belongs to circle"

    def in_triangle_out_circle(self,x_a, y_a, x_b, y_b, x_c, y_c, x, y):
       print(self.isInside(x_a, y_a, x_b, y_b, x_c, y_c, x, y), "b" )
       print(self.point_out_circle(x_a, y_a, x_b, y_b, x_c, y_c, x, y),"c")
       if self.isInside(x_a, y_a, x_b, y_b, x_c, y_c, x, y)==True and self.point_out_circle(x_a, y_a, x_b, y_b, x_c, y_c, x, y)==False:
           return "True"
       else:
           return "False"


if __name__ == '__main__':
    my_geometry= Geometry()
    print(my_geometry.distance(0,0,5,2))
    print(my_geometry.middle(0, 0, 5, 2))
    print(my_geometry.triangle_perimeter(0, 0, 2, 0,1,2))
    print(my_geometry.incircle_radius(0, 0, 2, 0,1,2))
    print(my_geometry.outcircle_radius(0, 0, 2, 0, 1, 2))
    print(my_geometry.in_triangle_out_circle(0, 0, 2, 0, 1, 2,1,0.3))
    print(my_geometry.centroid_point(0, 0, 2, 0,1,2)[1])