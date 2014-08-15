import unittest
from temperature import ftoc, ctof


class TemperatureConversionTest(unittest.TestCase):
    
    def F_to_C_conversions(self):
        self.assertEqual(0, ftoc(32))
        self.assertEqual(100, ftoc(212))
        self.assertEqual(37, ftoc(98.6))
        self.assertEqual(20, ftoc(68))
        
    def C_to_F_conversions(self):
        self.assertEqual(32, ctof(0))
        self.assertEqual(212, ctof(100))
        self.assertEqual(68, ctof(20))
        self.assertEqual(98.6, ctof(37))
        
        
if __name__ == '__main__':
    unittest.main()    