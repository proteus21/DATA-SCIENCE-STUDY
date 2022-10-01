"""
    Stwórz klasę Calculator, w ktorej zaimplementujesz dzialania:
    - dodawanie,
    - odejmowanie,
    - mnozenie,
    - dzielenie.
    Napisz testy, które przetestuja wczesniej wymienione metody.
"""

import unittest


class Calculator:
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

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator(1, 2)

    def test_additional(self):
        self.assertEqual(self.calc.additional(), 3)

    def test_substract(self):
        self.assertEqual(self.calc.substrack(), -1)


if __name__ == '__main__':
    unittest.main()