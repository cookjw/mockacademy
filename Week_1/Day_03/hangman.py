#Hangman
    #Word chosen randomly from list in .txt file.
    #"Body parts" represented by counter going up to 10.

#Select word at random from words.txt
    #Open file
    #Select line at random between 5 and 58114
    #Store word from selected line
    
#Display blank spaces corresponding to letters in word  
 
#Prompt player to enter guess    

#(etc.)

    
import random

f = open('words.txt')
wordlist = f.readlines()
wordnumber = random.randrange(5,58114)
word = wordlist[wordnumber][:-1]


def hangman():
    used_letters.append(guess)
    global counter
    counter += 1
    

def winning_condition():
    status = True
    for i in range(len(word)):
        if word[i] != revealed_letters[i]:
            status = False
    return status    
    
def losing_condition():
    if counter < 10:
        return False
    else:
        return True
            

used_letters = []
revealed_letters = []
counter = 1



for i in range(len(word)):
    revealed_letters.append("_")
 
while not (winning_condition() or losing_condition()):
    print "Word: "    
    print revealed_letters
    print "\n"
    print "Not in word: "
    print used_letters
    print "\n"
    print "Counter: " + str(counter) + " of 10"   
    guess = raw_input("Guess a letter. \n")
    reveal = revealed_letters[:len(revealed_letters)]
    # avoid binding one list to another, otherwise changing one will change the other!
    for i in range(len(word)):    
        if word[i] == guess:
            reveal[i] = guess
    if reveal == revealed_letters:        
        hangman()
        print "Not in word!"
    else:
        revealed_letters = reveal
        
        
        
if winning_condition():
    print "Congratulations, you win!"
    
if losing_condition():
    print "Sorry, you lose. The word was " + "\"" + word + "\"."
    
    
            
    
    

# print word
# print len(word) 



   
 


