import unittest, rpn_calculator

class RPNCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = rpn_calculator.RPNCalculator()
        
    def test_add_two_numbers(self):
        self.calculator.push(2)
        self.calculator.push(3)
        self.calculator.plus()
        self.assertEqual(self.calculator.value, 5)

    def test_add_three_numbers(self):
        self.calculator.push(2)
        self.calculator.push(3)
        self.calculator.push(4)
        self.calculator.plus()
        self.assertEqual(self.calculator.value, 7)
        self.calculator.plus()
        self.assertEqual(self.calculator.value, 9)
        
    def test_subtracts_second_number_from_first(self):
        self.calculator.push(2)
        self.calculator.push(3)
        self.calculator.minus()
        self.assertEqual(self.calculator.value, -1)
        
    def test_adds_and_subtracts(self):
        self.calculator.push(2)
        self.calculator.push(3)
        self.calculator.push(4)
        self.calculator.minus()
        self.assertEqual(self.calculator.value, -1)
        self.calculator.plus()
        self.assertEqual(self.calculator.value, 1)
        
    def test_multiplies_and_divides(self):
        self.calculator.push(2)
        self.calculator.push(3)
        self.calculator.push(4)
        self.calculator.divide()
        self.assertEqual(self.calculator.value, (3.0/4.0)) 
        self.calculator.times()
        self.assertEqual(self.calculator.value, 2*(3.0/4.0))  

    def test_resolves_operator_precedence_unambiguously(self):
        # 1 2 + 3 * => (1 + 2) * 3
        self.calculator.push(1)
        self.calculator.push(2)
        self.calculator.plus()
        self.calculator.push(3)
        self.calculator.times()
        self.assertEqual(self.calculator.value, (1+2)*3)  
        
        # 1 2 3 * + => 1 + (2 * 3)
        self.calculator.push(1)
        self.calculator.push(2)
        self.calculator.push(3) 
        self.calculator.times()
        self.calculator.plus()
        self.assertEqual(self.calculator.value, 1+(2*3))
        
    def test_fails_informatively_when_not_enough_values(self):
        from rpn_calculator import EmptyCalculator
        self.assertRaises(EmptyCalculator, self.calculator.plus) #not self.calculator.plus() !
        self.assertRaises(EmptyCalculator, self.calculator.minus)
        self.assertRaises(EmptyCalculator, self.calculator.times)
        self.assertRaises(EmptyCalculator, self.calculator.divide)
        
    def test_tokenizes_string(self):
        self.assertEqual(self.calculator.tokens("1 2 3 * + 4 5 - /"), [1, 2, 3, "*", "+", 4, 5, "-", "/"])
        
    def test_evaluates_string(self):
        self.assertEqual(self.calculator.evaluate("1 2 3 * +"), ((2 * 3) + 1))
        self.assertEqual(self.calculator.evaluate("4 5 -"), (4 - 5))
        self.assertEqual(self.calculator.evaluate("2 3 /"), (2.0 / 3.0))
        self.assertEqual(self.calculator.evaluate("1 2 3 * + 4 5 - /"), (1.0 + (2 * 3)) / (4 - 5)) 
        
        
        
        
                
        





if __name__ == "__main__":
    unittest.main()