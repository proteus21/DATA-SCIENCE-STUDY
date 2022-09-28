import unittest
from polaczone_napisy import merge_strings




class Test_merge_string(unittest.TestCase):

    def test_merge_empty_and_full(self):
        string1, string2= "adam_","EWA"
        self.assertEqual(merge_strings(string1, string2),"adam_EWA")

    def test_merge_empty_and_number(self):
        string1, string2 = "adam_", 333
        self.assertEqual(merge_strings(string1, string2),"adam_333")




if __name__ == '__main__':
    unittest.main()
