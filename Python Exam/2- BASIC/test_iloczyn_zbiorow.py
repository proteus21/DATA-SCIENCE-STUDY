import unittest
from iloczyn_zbiorow import find_common_numbers




class TestEvenNumbers(unittest.TestCase):

    def test_common_number_sets(self):
        sets1, sets2 = ((1,2,3,4),(2,3,5,6))
        self.assertEqual(find_common_numbers(sets1, sets2),set())
    def test_no_sets(self):
        sets1=set()
        sets2 = ((1,2,3,4))
        self.assertEqual(find_common_numbers(sets1, sets2),set())

    def test_common_number_three_sets(self):
        sets1 = ((1, 2, 3, 4),(2, 3, 5, 6),(2,5,6,8))
        sets2 = ((1, 2, 3, 4), (2, 3, 5, 6), (2, 5, 6, 8))
        self.assertEqual(find_common_numbers(sets1, sets2), {1,2})


if __name__ == '__main__':
    unittest.main()
