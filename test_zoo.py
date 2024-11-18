import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(17), 100)
    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(40), 150)
    def test_older_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(80), 100)
if __name__ == '__main__':
    unittest.main()