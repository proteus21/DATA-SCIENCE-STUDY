"""
    Stwórz klasę o nazwie Rectangle.
    Klasa powinna mieć dwa pola dla boków oraz metodę area (property) do liczenia pola prostokąta.
"""
class Rectangle:
    def __init__(self,side_a,side_b):
        self.side_a=side_a
        self.side_b=side_b
    @property
    def area(self):
        rect=self.side_a*self.side_b
        return rect

if __name__=="__main__":
  a,b =(input("Give a and  b and split with coma them:").split(","))

  area_rect=Rectangle(int(a) ,int(b))
  print("Rectangle area is {}".format(str(area_rect.area)))
