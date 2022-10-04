class Car():
    def __init__(self, brand, model,colour,year):
        self.brand =brand
        self.model=model
        self.colour=colour
        self.year=year

    def honk(self):
        return self.brand
    def show_details(self):
        return f"My car {self.model} has  {self.colour} and {self.year} colour "


if __name__ == '__main__':
    @set
    a=Car("ford","fiesta","yellow",1910)
    b=Car("VW","golf","green",2020)
    c = Car("Fiat", "126", "green", 1920)


    print(a.show_details())
    c.year=2025
    print(c.show_details())

