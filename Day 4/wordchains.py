# Word Chains: "Find a way to mutate a dictionary word into another of the same length by changing one letter at a time,
# with all the intermediaries also being valid words (e.g., *duck* to unprintable to *funk* to *fund*).

# CURRENT STATUS: Does job, but need to refine output

import string


f = open("..\Day 3\dictionary.txt")
wordlist = f.readlines()
f.close()

def mutate(word, letter_index):
    mutations = [word]
    for letter in string.ascii_lowercase:
        attempt = list(word)
        attempt[letter_index] = letter
        attempt = "".join(attempt) + '\n'
        if attempt in wordlist and attempt[:-1] != word:
            mutations.append(attempt[:-1])
    return mutations        


        
def wordchain(origin_word, target_word):
    if len(origin_word) != len(target_word):
        print "Sorry, words must be same length!"
    else:              
        wordlength = len(origin_word)    
        differlist = [i for i in range(wordlength) if origin_word[i] != target_word[i]]                        
        for i in differlist:
            for word in mutate(origin_word, i):
                if word == target_word:
                    print word                    
                elif word[i] == target_word[i]:
                    print word
                    wordchain(word, target_word)
                
        

print wordchain("duck", "fund")

print " "
        
print wordchain("bury", "fund")




     
                
            
        
