def translate(words):
    def checkcaps(word):
        if [letter for letter in word if letter == letter.upper()] != []:
            return word.capitalize()
        else:
            return word
            
    if len(words.split(' ')) > 1:
        translist = []
        for word in words.split(' '):
            translist.append(translate(word))
        return ' '.join(translist)
    elif "..." in words:
        translist = [translate(word) for word in words.split('...')]
        return '...'.join(translist)             
    else:
        word = words
        def rightpunctuation(word):
            if word != "..." and word[-1] in [".", "?", "!", ",", ";", "--", "\"", "\'", ")"]:
                return word[-1]
            else:
                return ""
        def leftpunctuation(word):
            if word[0] in ["\"", "(", "\'"]:
                return word[0]
            else:
                return ""            
        def chop_punctuation(word):
            if rightpunctuation(word) != "":
                return chop_punctuation(word[:-1])
            elif leftpunctuation(word) != "":
                return chop_punctuation(word[1:])
            else:
                return word
         
        word_with_punctuation = word
        word = chop_punctuation(word)            
        vowels = ['a', 'e', 'i', 'o', 'u']
        if word[0] in vowels:
            output = word + 'ay'
        elif word[0:2] == "ch":
            output = word[2:] + 'ch' + 'ay'
        elif word[0:2] == 'qu':
            output = word[2:] + 'qu' + 'ay'
        elif not (word[0] in vowels) and not (word[1] in vowels) and not (word[2] in vowels):
            output = word[3:] + word[0:3] + 'ay'
        elif (not (word[0] in vowels)) and word[1:3] == "qu":
            output = word[3:] + word[0:3] + 'ay'
        elif not (word[0] in vowels) and not (word[1] in vowels):
            output = word[2:] + word[0:2] + 'ay'
        else:
            output = word[1:] + word[0] + 'ay' 
        return leftpunctuation(word_with_punctuation) + checkcaps(output)  + rightpunctuation(word_with_punctuation)   


        
            
            