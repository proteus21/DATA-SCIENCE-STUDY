import random
contact_list=[]
class Calculator:
    #init is not neccesery
    def __init__(self,value_x, value_y):
       self.value_x=int(value_x)
       self.value_y = int(value_y)
    def additional(self):
        return(self.value_x+self.value_y)
    def substrack(self):
        return (self.value_x - self.value_y)
    def multiple(self):
        return (self.value_x * self.value_y)
    def divide(self):
        return (self.value_x / self.value_y)

# second solution
class Calculator_1:
    #init is not neccesery

    def additional(self, x, y):
        return x + y
    def substrack(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        return x /y

if __name__ == '__main__':
    calc=Calculator(5,2) # tylko na tych liczbach
    print(calc.additional())
    print(calc.multiple())
    calc1=Calculator_1()
    print(calc1.additional(5, 4))
    print(calc1.divide(16, 4))


class Person:
    def __init__(self, first_name, last_name, number):
        self.first_name= first_name
        self.last_name= last_name
        self.number=number
    def call(self):
        return f"Call to {self.first_name} {self.last_name} {self.number}"

if __name__ == '__main__':
    call=Person("Nick","Trevor",45748574)
    print(call.call())


#Simple solution
class TeleBook:

    def __init__(self, contacts):
        self.contacts = contacts

    def add(self, person):
        self.contacts.append(person)

    def remove(self, person):
        self.contacts.remove(person)

    def call_random(self):
        return random.choice(self.contacts).call()


if __name__ == '__main__':
    doda = Person("Dorota", "Rabczewska", "777777777")
    krzysztof = Person("Krzysztof", "Krawczyk", "000000000")
    jas = Person("Jaś", "Fasola", "123123123")
    telebook = TeleBook([doda, krzysztof, jas])
    print(telebook.contacts)
    maryla = Person("Maryla", "Rodowicz", "999999999")
    telebook.add(maryla)
    print(telebook.contacts)
    telebook.remove(jas)
    print(telebook.contacts)
    print(telebook.call_random())
    print(telebook.call_random())
    print(telebook.call_random())
    print(telebook.call_random())
    print(telebook.call_random())
    print(telebook.call_random())



