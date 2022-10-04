'''
Create a class Person with attributes: name and age
- Create a display() method that displays the name and age of an object created via the Person class.
- Create a child class Student which inherits from the Person class and which also has a section
attribute.
- Create a method display_student() that displays the name, age and section of an object created via
the Student class.
- Create a student object via an instantiation on the Student class and then test the display_student
method.
'''

class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def display(self):# jesli to czynnosc to zostawiamy funkcja a gdy bedzie jako rzecz, detale bedzie @property
        return f"The person name {self.name} and has {self.age}"


class Student(Person):
    def __init__(self,name, age, section):
        super().__init__(name,age)
        self.section = section
    def display_student(self):
        return super().display() + f", Section: {self.section}"



if __name__ == '__main__':
   p= Person("Michal",45)
   print(p.display())
   s= Student("Michal",45, "Math")
   print(s.display_student())
