import unittest
from EigerQuestion1 import priceCheck



class TestPriceCheck(unittest.TestCase):

    def test1_price_check(self):
        res = priceCheck(products=['rice', 'sugar', 'wheat', 'cheese'],
                         productPrices=[16.89, 56.92, 20.89, 345.99],
                         productSold=['rice', 'cheese'],
                         soldPrice=[18.99, 400.89])
        self.assertEqual(2, res)

    def test2_price_check(self):
        res = priceCheck(products=['eggs', 'milk', 'cheese'],
                         productPrices=[2.89, 3.29, 5.79],
                         productSold=['eggs', 'eggs', 'cheese', 'milk'],
                         soldPrice=[2.89, 2.99, 5.97, 3.29])
        self.assertEqual(2, res)

    def test3_price_check(self):     #example for a test that I added
        res = priceCheck(products=['tea', 'coffee', 'juice'],
                         productPrices=[10.89, 15.87, 10.55],
                         productSold=['tea', 'coffee', 'tea','juice', 'juice'],
                         soldPrice=[10.89, 15.88, 10.90, 10.55, 10.56])
        self.assertEqual(3, res)



if __name__ == '__main__':
    unittest.main()
