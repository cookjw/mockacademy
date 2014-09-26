class Temperature:

    @classmethod
    def ftoc(cls, f):
        return (5.0/9.0)*(f - 32)
        
    @classmethod
    def ctof(cls, c):
        return (9.0/5.0)*c + 32
        
    def __init__(self, f=None, c=None):        
        self.F = f        
        self.C = c
        
    def in_fahrenheit(self):
        if self.F is not None:
            return self.F            
        elif self.C is not None:
            return Temperature.ctof(self.C)  
        
            
    def in_celsius(self):
        if self.C is not None:
            return self.C    
        elif self.F is not None:
            return Temperature.ftoc(self.F)
            
    @classmethod
    def from_celsius(cls, degrees):
        temp = Temperature(c=degrees)
        return temp
        
    @classmethod
    def from_fahrenheit(cls, degrees):
        temp = Temperature(f=degrees)
        return temp
        
class Celsius(Temperature):
    def __init__(self, number):
        Temperature.__init__(self, c=number)
        
class Fahrenheit(Temperature):
    def __init__(self, number):
        Temperature.__init__(self, f=number)
    

            
        
            
    
        
    