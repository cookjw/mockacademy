
def name(magnitude):
    if magnitude == 0:
        return "" 
    elif magnitude == 1:
          return "thousand"
    elif magnitude == 2:
        return "million"
    elif magnitude == 3:
        return "billion"
    elif magnitude == 4:
        return "trillion"
    elif magnitude == 5:
        return "quadrillion"
    elif magnitude == 6:
        return "quintillion"
    elif magnitude == 7:
        return "sextillion"
    elif magnitude == 8:
        return "septillion"
    elif magnitude == 9:
        return "octillion"
    elif magnitude == 10:
        return "nonillion"  
    elif magnitude == 11:
        return "decillion" 


def underthousand(number):
    num = str(number)
    if len(num) == 1:
        if num == "0":
            return "zero"
        elif num == "1":
            return "one"
        elif num == "2":
            return "two"
        elif num == "3":
            return "three"
        elif num == "4":
            return "four"
        elif num == "5":
            return "five"
        elif num == "6":
            return "six"
        elif num == "7":
            return "seven"
        elif num == "8":
            return "eight"
        elif num == "9":
            return "nine"

    elif len(num) == 2:
        tens = num[0]
        ones = num[1]
        if tens == "1":
            if ones == "0":
                return "ten"
            elif ones == "1":
                return "eleven"
            elif ones == "2":
                return "twelve"
            elif ones == "3":
                return "thirteen"
            elif ones == "4":
                return "fourteen"
            elif ones == "5":
                return "fifteen"
            elif ones == "6":
                return "sixteen"
            elif ones == "7":
                return "seventeen"
            elif ones == "8":
                return "eighteen"
            else:
                return underthousand(int(ones)) + "teen"
                
        elif tens == "2":
            if ones == "0":
                return "twenty"
            else:
                return "twenty " + underthousand(int(ones))
                
        elif tens == "3":
            if ones == "0":
                return "thirty"
            else:
                return "thirty " + underthousand(int(ones))
                
        elif tens == "4":
            if ones == "0":
                return "forty"
            else:
                return "forty " + underthousand(int(ones))  

        elif tens == "5":
            if ones == "0":
                return "fifty"
            else:
                return "fifty " + underthousand(int(ones))  

        elif tens == "6":
            if ones == "0":
                return "sixty"
            else:
                return "sixty " + underthousand(int(ones))  

        elif tens == "7":
            if ones == "0":
                return "seventy"
            else:
                return "seventy " + underthousand(int(ones))  

        elif tens == "8":
            if ones == "0":
                return "eighty"
            else:
                return "eighty " + underthousand(int(ones))  

        elif tens == "9":
            if ones == "0":
                return "ninety"
            else:
                return "ninety " + underthousand(int(ones))   

    elif len(num) == 3:
        if num[1] == "0" and num[2] == "0":
            return underthousand(int(num[0])) + " hundred"
        elif num[1] == "0":
            return underthousand(int(num[0])) + " hundred" + " " + underthousand(int(num[2]))
        else:
            return underthousand(int(num[0])) + " hundred" + " " + underthousand(int(num[1:]))
            
            
def in_words(number):
    num = str(number)
    num_digits = len(num)
    magnitude = num_digits/3
    revnum = num[::-1]
    segments = []
    for k in range(magnitude):
        segments.append(revnum[3*k:3*k + 3])
    if num_digits % 3 != 0:
        segments.append(revnum[3*magnitude:])
        
    if magnitude == 0:
        segments = [revnum]
    name_indices = []
    for i in range(len(segments)):
        if segments[i] != "000":
            name_indices.append(i)
    
    def space_ifnec(i):
        if i == 0:
            return "" 
        else:
            return " "

    names = [underthousand(int(segments[i][::-1])) + space_ifnec(i) + name(i) for i in name_indices]  
    revnames = names[::-1]
    number = revnames[0]
    for x in revnames[1:]:
        number = number + " " + x 
    return number        
        
            
             
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                 