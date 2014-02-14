#Spelling out numbers:
    #Divide digits by 3, find remainder
    #Determine appropriate magnitude (which -illion leads) (will go to decillions)
    #List descending magnitudes (...trillion, billion, million, thousand, ---), skipping "000"'s

def name(magnitude):
    if magnitude == 0:
        return "" 
    if magnitude == 1:
        return "thousand"
    if magnitude == 2:
        return "million"
    if magnitude == 3:
        return "billion"
    if magnitude == 4:
        return "trillion"
    if magnitude == 5:
        return "quadrillion"
    if magnitude == 6:
        return "quintillion"
    if magnitude == 7:
        return "sextillion"
    if magnitude == 8:
        return "septillion"
    if magnitude == 9:
        return "octillion"
    if magnitude == 10:
        return "nonillion"  
    if magnitude == 11:
        return "decillion"    

def underthousand(n): #spelling out numbers under 1000, taken from my solution to Project Euler problem 17.
    num = str(n)
    if len(num) == 1:
        if num == "1":
            return "one"
        if num == "2":
            return "two"
        if num == "3":
            return "three"
        if num == "4":
            return "four"
        if num == "5":
            return "five"
        if num == "6":
            return "six"
        if num == "7":
            return "seven"
        if num == "8":
            return "eight"
        if num == "9":
            return "nine"
    if len(num) == 2:
        tens = num[0]
        ones = num[1]
        if tens == "1":
            if ones == "0":
                return "ten"
            if ones == "1":
                return "eleven"
            if ones == "2":
                return "twelve"
            if ones == "3":
                return "thirteen"
            if ones == "4":
                return "fourteen"
            if ones == "5":
                return "fifteen"
            if ones == "8":
                return "eighteen"
            else:
                return underthousand(int(ones)) + "teen"
        if tens == "2":
            if ones == "0":
                return "twenty"
            else:
                return "twenty "+underthousand(int(ones))
        if tens == "3":
            if ones == "0":
                return "thirty"
            else:
                return "thirty " + underthousand(int(ones))
        if tens == "4":
            if ones == "0": 
                return "forty"
            else:
                return "forty " + underthousand(int(ones))
        if tens == "5":
            if ones == "0":
                return "fifty "
            else:
                return "fifty " + underthousand(int(ones))
        if tens == "8":
            if ones == "0":
                return "eighty "
            else:
                return "eighty " + underthousand(int(ones))
        else:
            if ones == "0":
                return underthousand(int(tens))+ "ty"
            else:
                return underthousand(int(tens)*10) + " " + underthousand(int(ones))
    if len(num) == 3:
        if num[1] == "0" and num[2] == "0":
            return underthousand(int(num[0])) + " hundred"
        elif num[1] == "0":
            return underthousand(int(num[0])) + " hundred" + " and " + underthousand(int(num[2]))
        else:
            return underthousand(int(num[0])) + " hundred" + " and " + underthousand(num[1:])
        
def spellout(n): 
    num = str(n)    
    num_digits = len(num)
    magnitude = num_digits/3
    revnum = num[::-1]
    #gather three-digit segments into a list:
    segments = []    
    for k in range(magnitude):
        segments.append(revnum[3*k:3*k+3])
    names = [underthousand(int(segments[i][::-1])) + " " + name(i) for i in range(len(segments)) if segments[i]!= "000"]
    revnames = names[::-1]
    number = revnames[0]
    for x in revnames[1:]:
        number = number + ", " + x 
    return number
    
print spellout(259123)   

print spellout(12345678909876543210) 

print spellout(100000000000001)
    
    
    
    
    
    
    




