class Employee:
    def __init__(self, name, surname, salary):
        self.name= name
        self.surname= surname
        self. salary= salary
    def show_details(self):
        return f"Employee name {self.name}, {self.surname} Employee salary is{self.salary}"
class Devaloper(Employee): # Do dziedziczenia kopiujemy pola  ktore dziedziczyma a do loczenia stosuje funkcji super()
    def __init__(self, name, surname, salary,language):
        super().__init__(name, surname, salary)
        self.language= language

    def show_details(self):
       return  super().show_details()+f"Programming langague:{self.language}"

class MyManger(Employee):
    def __init__(self,name, surname, salary,team ):
        super().__init__(name, surname, salary)
        self.team = team
    def show_details(self):
       return  super().show_details()+f"Team:{self.team}"

if __name__ == '__main__':
    piotr= Employee( "Piotr","Malinowski", 1000)
    print(piotr.show_details())
    piotr_developer= Devaloper("Piotr","Malinowski", 1000, "Python")
    print(piotr_developer.show_details())
    piotr_manager = MyManger("Piotr", "Malinowski", 1000, "IT")
    print( piotr_manager.show_details())