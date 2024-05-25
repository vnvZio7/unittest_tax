import unittest
import tax
class Test_Tax(unittest.TestCase):
    
    def test_tax_calculation(self):
        self.assertEqual(tax.tax_calculation(10000000, 0), 0)               # Trường hợp không phải chịu thuế (5% của 0 triệu)
        self.assertEqual(tax.tax_calculation(15000000, 0), 200000)          # Trường hợp tính thuế 5% 
        self.assertEqual(tax.tax_calculation(20000000, 0), 650000)          # Trường hợp tính thuế 10% 
        self.assertEqual(tax.tax_calculation(27000000, 1), 990000)          # Trường hợp tính thuế 15% 
        self.assertEqual(tax.tax_calculation(40000000, 2), 2390000)         # Trường hợp tính thuế 20% 
        self.assertEqual(tax.tax_calculation(60000000, 3), 5700000)         # Trường hợp tính thuế 25% 
        self.assertEqual(tax.tax_calculation(90000000, 3), 13890000)        # Trường hợp tính thuế 30% 
        self.assertEqual(tax.tax_calculation(1000000000, 10), 320900000)    # Trường hợp tính thuế 35% 
        with self.assertRaises(ValueError):
            tax.tax_calculation(3000000, -1)    # Trường hợp số người phụ thuộc không hợp lệ 
            tax.tax_calculation(-1, -1)         # Trường hợp thu nhập cá nhân và số người phụ thuộc không hợp lệ 
            tax.tax_calculation(-1, 1)          # Trường hợp thu nhập cá nhân không hợp hệ

if __name__ == "__main__":
    unittest.main()