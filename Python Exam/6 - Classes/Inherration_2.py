class Human:

    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age = age

    def __repr__(self):
        return f"{self.__class__.__name__} " \
               f"Weight: {self.weight}, " \
               f"Height: {self.height}, " \
               f"Age: {self.age}"


class Cook(Human):

    def __init__(self, weight, height, age, cuisine):
        super().__init__(weight, height, age)
        self.cuisine = cuisine

    def prepare_dish(self, dish):
        return f"Cooking {self.cuisine} {dish}"

    def __repr__(self):
        # super repr wywoluje co poprzednio i dodajemy na nowe. Odwołanie do klasy wyzej
        return super().__repr__()+f",Cuisine:{self.cuisine}"


if __name__ == '__main__':
    human = Human(100, 170, 18)
    gordon_ramsay = Cook(98, 185, 34, "Italian")
    print(human)
    print(gordon_ramsay)
    print(gordon_ramsay.prepare_dish("Pizza"))
