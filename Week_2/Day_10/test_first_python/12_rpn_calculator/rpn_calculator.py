def arithmetic(op, a, b):
    if op == "plus":
        return a + b    
  
    elif op == "minus":
        return a - b

    elif op == "times":
        return a * b

    elif op == "divide":
        return a / b
        
class RPNCalculator:
    def __init__(self):
        self.inputlist = []
        self.value = 0.0
     
    def push(self, input):
        self.inputlist.append(float(input))
        
    def operation(self, opname):
        if len(self.inputlist) >= 2:
            things = self.inputlist[-2:]
            self.inputlist = self.inputlist[:-2]
            self.value = arithmetic(opname, things[0], things[1])
            self.push(self.value)
            return self.value
        else:
            raise EmptyCalculator("calculator is empty")
             
    def plus(self):
        return self.operation("plus")
        
    def minus(self):
        return self.operation("minus")
        
    def times(self):
        return self.operation("times")
        
    def divide(self):
        return self.operation("divide")
        
    def tokens(self, input):
        def string(x):
            if x.isdigit():
                return int(x)
            else:
                return x
        return [string(x) for x in input.split(' ')]
        
    def evaluate(self, input):
        putin = self.tokens(input)
        for x in putin:
            if isinstance(x, int) or isinstance(x, float):
                self.push(x)
            elif x == "+":
                self.plus()
            elif x == "-":
                self.minus()
            elif x == "*":
                self.times()
            elif x == "/":
                self.divide()
        return self.value
        
class EmptyCalculator(Exception):
    pass
                
        
            
        
    
        
             