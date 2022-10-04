from random import choice
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
        return choice(self.contacts).call()


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



