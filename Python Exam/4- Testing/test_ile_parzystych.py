import unittest
from ile_parzystych import count_even_numbers


class TestEvenNumbers(unittest.TestCase):

    def test_few_numbers_from_the_list_are_even(self):
        numbers = [3, 6, 1, 1, 8, 3, 4]
        evens_amount = count_even_numbers(numbers)
        self.assertEqual(evens_amount, 3)

    def test_all_numbers_from_the_list_are_even(self):
        numbers = [2, 4, 6, 8, 10]
        evens_amount = count_even_numbers(numbers)
        self.assertEqual(evens_amount, 5)

    def test_no_even_numbers_in_the_list(self):
        numbers = [55, 7, 19, 21]
        evens_amount = count_even_numbers(numbers)
        self.assertEqual(evens_amount, 0)

    def test_no_numbers_in_the_list_and_no_evens(self):
        numbers = []
        evens_amount = count_even_numbers(numbers)
        self.assertEqual(evens_amount, 0)

    def test_numbers_with_zero_inside_the_list(self):
        numbers = [3, 16, 0, 1, 4, 0, 23]
        evens_amount = count_even_numbers(numbers)
        self.assertEqual(evens_amount, 4)


if __name__ == '__main__':
    unittest.main()
