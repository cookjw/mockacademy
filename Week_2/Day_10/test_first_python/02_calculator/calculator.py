def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y
    
def sum(*array):
    total = 0
    for n in array:
        total = total + n
    return total

def multiply(*list):
    product = 1
    for n in list:
        product = product*n
    return product
    
def power(x, y):
    return x**y
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
