import unittest, temperature
from temperature import Temperature, Celsius, Fahrenheit

class TemperatureTest(unittest.TestCase):
    def test_50_degrees_f(self):
        self.assertEqual(Temperature(f=50).in_fahrenheit(), 50)
        
    def test_convert_freezing_to_celsius(self):
        self.assertEqual(Temperature(f=32).in_celsius(), 0)
        
    def test_convert_boiling_to_celsius(self):
        self.assertEqual(Temperature(f=212).in_celsius(), 100)
        
    def test_convert_body_temperature_to_celsius(self):
        self.assertEqual(Temperature(f=98.6).in_celsius(), 37)
        
    def test_convert_arbitrary_temperature_to_celsius(self):
        self.assertEqual(Temperature(f=68).in_celsius(), 20)
        
    def test_50_degrees_c(self):
        self.assertEqual(Temperature(c=50).in_celsius(), 50)
        
    def test_convert_freezing_to_fahrenheit(self):
        self.assertEqual(Temperature(c=0).in_fahrenheit(), 32)
        
    def test_convert_boiling_to_fahrenheit(self):
        self.assertEqual(Temperature(c=100).in_fahrenheit(), 212)
        
    def test_convert_body_temperature_to_fahrenheit(self):
        self.assertAlmostEqual(Temperature(c=37).in_fahrenheit(), 98.6, delta=0.1)
        
    def test_factory_celsius(self): #"factory method"
        self.assertEqual(Temperature.from_celsius(50).in_celsius(), 50)
        self.assertEqual(Temperature.from_celsius(50).in_fahrenheit(), 122)
        
    def test_factory_fahrenheit(self): #"factory method"
        self.assertEqual(Temperature.from_fahrenheit(50).in_fahrenheit(), 50)
        self.assertEqual(Temperature.from_fahrenheit(50).in_celsius(), 10)
        
class TemperatureSubclasses(unittest.TestCase):
    def test_celsius_construct(self):
        self.assertEqual(Celsius(50).in_celsius(), 50)
        self.assertEqual(Celsius(50).in_fahrenheit(),122)
        
    def test_celsius_Temperature_subclass(self):
        self.assertIsInstance(Celsius(50), Temperature)
        
    def test_fahrenheit_construct(self):
        self.assertEqual(Fahrenheit(50).in_fahrenheit(), 50)
        self.assertEqual(Fahrenheit(50).in_celsius(), 10)
        
    def test_fahrenheit_Temperature_subclass(self):
        self.assertIsInstance(Fahrenheit(50), Temperature)
        
    
        
        
    







if __name__ == "__main__":
    unittest.main()