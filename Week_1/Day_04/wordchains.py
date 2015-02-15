# Word Chains: "Find a way to mutate a dictionary word into another of 
# the same length by changing one letter at a time,
# with all the intermediaries also being valid words
# (e.g., *duck* to unprintable to *funk* to *fund*).

# CURRENT STATUS: (apparent) TRIUMPH! 

import string


f = open("..\Day_03\dictionary.txt")
wordlist = f.readlines()
f.close()

def mutate(word, letter_index):
    mutations = []
    for letter in string.ascii_lowercase:
        attempt = list(word)
        attempt[letter_index] = letter
        attempt = "".join(attempt) + '\n'
        if attempt in wordlist and attempt[:-1] != word:
            mutations.append(attempt[:-1])
    return mutations        


        

import Queue
        

def wordchain(origin_word, target_word):
    if len(origin_word) != len(target_word):
        print "Sorry, words must be same length!"     
    else:
        Q = Queue.Queue()        
        A = {} # for "Ancestor"
        Q.put(origin_word)        
        while not Q.empty():
            word = Q.get()            
            if word == target_word:                
                revchain = [target_word]
                w = target_word
                while w != origin_word:
                    revchain.append(A[w])
                    w = A[w]           
                chain = revchain[::-1]
                return chain                    
            else:
                for letter_index in range(len(word)):
                    for wordie in mutate(word, letter_index):
                        if not wordie in A:                            
                            A[wordie] = word
                            Q.put(wordie)

                            
origin_word = raw_input("Enter starting word: \n")
target_word = raw_input("Enter target word: \n")

chain = [origin_word]

print " "

print wordchain(origin_word, target_word)




     
                
            
        
