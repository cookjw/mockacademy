import unittest
from silly_decorators import reverser, adder, repeater


class SillyTest(unittest.TestCase):
    def test_reverser(self):
        @reverser
        def hello(name=""):
            if name == "":
                return "hello"
            else:
                return "hello" + " " + name            
        
        self.assertEqual(hello(), "olleh")
        self.assertEqual(hello("dolly"), "olleh yllod")
        

    def test_adder(self):
        @adder
        def five(number=0):
            return 5
        
        self.assertEqual(five(0), 5)
        self.assertEqual(five(3), 8)        

        
    def test_repeater(self):
        stuff_was_executed = [False] # hack courtesy of http://stackoverflow.com/questions/291978/short-description-of-python-scoping-rules?rq=1
        @repeater
        def execute():
            stuff_was_executed[0] = True           
            
        execute()         
        self.assertEqual(stuff_was_executed[0], True)
        
        n = [0] 
        @repeater
        def increase_n():
            n[0] += 1
        
        increase_n(3)        
        self.assertEqual(n[0], 3)
        
        n = [0]
        increase_n(10)
        self.assertEqual(n[0], 10)







if __name__ == "__main__":
    unittest.main()