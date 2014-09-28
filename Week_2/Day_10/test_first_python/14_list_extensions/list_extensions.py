class Array(list):
    def __init__(self, *args):
        for element in args:
            self.append(element)
            
    def sum(self):
        s = 0
        for x in self:
            s = s + x
        return s
        
    def square(self):
        return [x*x for x in self]
        
    def SQUARE(self):
        squares = self.square()
        for i in range(len(self)):
            self[i] = squares[i]
            
            