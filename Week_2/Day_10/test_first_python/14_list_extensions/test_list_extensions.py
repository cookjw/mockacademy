import unittest
from list_extensions import Array

class ArraySumTest(unittest.TestCase):
    def test_sum_method(self):
        self.assertTrue(hasattr(Array(), "sum"))
    
    def test_0_for_empty_array(self):
        self.assertEqual(Array().sum(),0)
        
    def test_add_all_the_elements(self):
        self.assertEqual(Array(1,2,4).sum(), 7)        

class ArraySquareTest(unittest.TestCase):
    def test_does_nothing_to_empty(self):
        A = Array()
        self.assertEqual(A.square(), [])
        
    def test_returns_new_array_containing_squares(self):
        A = Array(1,2,3)
        self.assertEqual(A.square(), [1,4,9]) 
    

class ArraySQUARETest(unittest.TestCase): # yeah I know this replacement for "!" isn't the "proper convention", but it amuses me
    def test_squares_each_element(self):
        array = Array(1,2,3)
        array.SQUARE()
        self.assertEqual(array, [1,4,9])
    


if __name__ == "__main__":
    unittest.main()