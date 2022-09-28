import unittest
from cena_brutto import calculate_brutto_prize




class TestEvenNumbers(unittest.TestCase):

    def test_calculate_brutto_price_with_diffrent_tax(self):
        glocary_list = {"mleko": (5.00, 10), "ser": (4.50, 15), "jogurt": (3, 25)}
        prize = calculate_brutto_prize(glocary_list)
        self.assertEqual(prize, 14)
    def test_no_product_prize(self):
        grocery_list = {}
        prize = calculate_brutto_prize(grocery_list)
        self.assertEqual(prize, 0)

    def test_one_product_prize_with_tax_zero(self):
        grocery_list = {"mleko": (5.00, 0)}
        prize = calculate_brutto_prize(grocery_list)
        self.assertEqual(prize, 5)
    def test_one_product_prize_with_tax_fifty(self):
        grocery_list = {"mleko": (5.00, 50)}
        prize = calculate_brutto_prize(grocery_list)
        self.assertEqual(prize, 0)

if __name__ == '__main__':
    unittest.main()
