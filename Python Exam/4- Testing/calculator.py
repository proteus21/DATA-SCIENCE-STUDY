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
    def test_additional(self):

        self.assertEqual(additional(1,2), 3)

    def test_substract(self):

        self.assertEqual(substrack(3,1), 2)


if __name__ == '__main__':
    unittest.main()