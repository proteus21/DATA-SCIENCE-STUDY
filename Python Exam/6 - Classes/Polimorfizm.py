class Parrot:

    @staticmethod
    def fly():
        return "Parrots can fly."

    @staticmethod
    def swim():
        return "Parrots don't swim!"


class Penguin:

    @staticmethod
    def fly():
        return "Penguins don't fly."

    @staticmethod
    def swim():
        return "Penguins can swim!"


def flying_test(bird):
    return bird.fly()


def swimming_test(bird):
    return bird.swim()


if __name__ == '__main__':
    blu = Parrot()
    peggie = Penguin()
    print(flying_test(blu))
    print(flying_test(peggie))
    print(swimming_test(blu))
    print(swimming_test(peggie))