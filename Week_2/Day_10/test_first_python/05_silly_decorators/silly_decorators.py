
def reverser(function):
    def argument_accessor(*args):
        outputlist = []
        for word in function(*args).split(' '):
            outputlist.append(word[::-1])
        return ' '.join(outputlist)
    return argument_accessor
    
    
def adder(function):
    def argument_accessor(number=0, *args):
        return function(*args) + number
    return argument_accessor


def repeater(function):
    def argument_accessor(times=1, *args):        
        for n in range(times):
            function(*args)        
    return argument_accessor
            
       
            