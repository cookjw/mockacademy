def echo(input):
    return input
    
def shout(input):
    return input.upper()
    
def repeat(input, times=2):
    n = times
    output = input
    while n > 1:
        output = output + " " + input
        n = n - 1
    return output

def start_of_word(word, number=1):
    return word[0:number]

def first_word(string):
    return string.split(" ")[0]

def titleize(title):
    smallwords = ["and", "the", "in", "an", "or", "at", "of", "a", "over"] #list not comprehensive, but what am I to do...?
    titlewords = title.split(' ')
    newtitlewords = []
    for index in range(len(titlewords)):
        word = titlewords[index]
        if not (word in smallwords and index != 0):
            new_word = word.capitalize()
            newtitlewords.append(new_word)
        else:
            newtitlewords.append(word)
    newtitle = ' '.join(newtitlewords)
    return newtitle
        
        

    
    
    


