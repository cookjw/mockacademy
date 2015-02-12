import string

def cipher(input, number):
    inputlist = list(input)
    for position in range(len(inputlist)):
        if inputlist[position] in string.ascii_lowercase:
            inputlist[position] = string.ascii_lowercase[(
                string.ascii_lowercase.index(inputlist[position])+number
                )%26]
        if inputlist[position] in string.ascii_uppercase:
            inputlist[position] = string.ascii_uppercase[(
            string.ascii_uppercase.index(inputlist[position])+number
            )%26]        
    outputstring = "".join(inputlist)
    return outputstring    
    
    
text = raw_input("Enter text. \n")

number = int(raw_input("Enter number. \n"))

print cipher(text, number)