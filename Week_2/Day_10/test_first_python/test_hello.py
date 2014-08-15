import unittest
from hello import hello, greet

class HelloTest(unittest.TestCase):
    
    def test_hello(self):
        self.assertEqual("Hello!", hello()) 
        
    def test_greet(self):
        self.assertEqual("Hello, Alice!", greet("Alice")) 
        self.assertEqual("Hello, Bob!", greet("Bob")) 
        
if __name__ == '__main__':
    unittest.main()     