
def reverser(function):
    def wrapper(*args):
        outputlist = []
        for word in function(*args).split(' '):
            outputlist.append(word[::-1])
        return ' '.join(outputlist)
    return wrapper
    
    
def adder(function):
    def wrapper(*args):
        return function(*args) + sum([x for x in args])
    return wrapper


def repeater(function):
    def wrapper(times=1):        
        for n in range(times):
            function()        
    return wrapper
            
       
            