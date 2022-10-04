"""
    Dla funkcji odd_indexes napisanej ponizej,
    ktora dla zadanego stringa zwraca litery z nieparzystych indeksow, np:
    - teleturniej -> eeune
    - komputer -> optr,
    napisz testy dla argumentu, ktory bedzie stringiem.
    Uruchom funkcje przekazujac int.
    Zaobserwuj, co sie stalo.
    Napisz testy dla argumentow, ktore sa intem.
    Popraw funkcje by dzialala poprawnie, sprawiajac by testy przeszly.
"""

import unittest


def odd_indexes(string):
    return string[1::2]
    
    
class TestOddIndexes(unittest.TestCase):
    def test_odd_indexes(self):
        string="teleturniej"
        self.assertEqual(odd_indexes(string), "eeune")
    def test_even_indexes(self):
        string="teleturniej"
        self.assertEqual(odd_indexes(string), "tltrij")


if __name__ == '__main__':
    unittest.main() 