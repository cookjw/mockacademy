from string import ascii_uppercase

def digit(number):
    """
    Converts number to 'digit', i.e. appropriate single-character 
    string ('0' through '9', or 'A' through 'Z' for bases > 10)
    """
    if 0 <= number <= 9:
        return str(number)
    elif 10 <= number < 36:
        return ascii_uppercase[number - 10]
    else:
        raise Exception("Wrong kind of input for digit function")
        
def highest_power(number, base):
    """
    Returns highest power of base that is <= number
    (i.e., the floor function of the logarithm of number to base base)
    """
    exponent = 0
    while base**(exponent) <= number:
        exponent += 1
    return exponent - 1
    

def convert_base(number, base):
    """
    Converts number (integer) to string representation in new base
    """
    result = ""
    n = highest_power(number, base)
    x = number
    while n >= 0:
        quotient = x // base**n # Integer division, even in Python 3!
        remainder = x % base**n
        place_value = digit(quotient)
        result += place_value
        x = remainder
        n -= 1
    return result
    