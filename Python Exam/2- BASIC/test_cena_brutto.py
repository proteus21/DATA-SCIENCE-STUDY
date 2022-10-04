import unittest
from cena_netto import calculate_brutto_prize


class TestNettoPrize(unittest.TestCase):

    def test_one_product_with_10_percent_tax(self):
        grocery_list = {"apples": (12, 10)}
        prize = calculate_brutto_prize(grocery_list)
        self.assertEqual(prize, 10.8)

    def test_one_product_with_zero_percent_tax(self):
        grocery_list = {"apples": (12, 0)}
        prize = calculate_brutto_prize(grocery_list)
        self.assertEqual(prize, 12)

    def test_one_product_with_100_percent_tax(self):
        grocery_list = {"apples": (12, 100)}
        prize = calculate_brutto_prize(grocery_list)
        self.assertEqual(prize, 12)

    def test_two_products_with_different_percent_tax(self):
        grocery_list = {"apples": (12, 10), "milk": (4, 20)}
        prize = calculate_brutto_prize(grocery_list)
        self.assertEqual(prize, 14)

    def test_no_product_prize(self):
        grocery_list = {}
        prize = calculate_brutto_prizee(grocery_list)
        self.assertEqual(prize, 0)


if __name__ == '__main__':
    unittest.main()