import unittest
from calculator import add, subtract, sum, multiply, power, factorial

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(0,0), 0)   
        self.assertEqual(add(2,2), 4)
        self.assertEqual(add(2,6), 8)
                
    
    def test_subtract(self):
        self.assertEqual(subtract(10,4), 6)
    
    def test_sum(self):
        self.assertEqual(sum(), 0)
        self.assertEqual(sum(7), 7)
        self.assertEqual(sum(7,11), 18)
        self.assertEqual(sum(1,3,5,7,9), 25)
    
    def test_multiply(self):
        self.assertEqual(multiply(3,4), 12)
        self.assertEqual(multiply(3,4,5), 60)
    
    def test_power(self):   
        self.assertEqual(power(3,4), 81)    
    
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(5), 5*4*3*2*1)
        self.assertEqual(factorial(10), 10*9*8*7*6*5*4*3*2*1)
    
    
if __name__ == '__main__':
    unittest.main() 
    