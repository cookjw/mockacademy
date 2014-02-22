#Numerical Mastermind/Bulls and Cows

#Mastermind: codebreaker vs. codemaker
#Bulls and Cows: codemaker/breaker vs. codemaker/breaker

#Mastermind:
    #Choose number_of_guesses
    #Computer as codemaker:
        #Computer chooses number at random (digits must all be different)
        #Player has number_of_guesses attempts to guess number
            #Player guesses
            #Computer responds with feedback: bulls, cows

import random
            


def choosenumber(digits, choices):
    d = 1
    dlist = []
    while d <= digits:
        n = random.randrange(0, choices)
        while n in dlist:
            n = random.randrange(0, choices)
        dlist.append(n)
        d += 1
    return dlist
    
def bulls_and_cows():
    global guess_strings, guess, guesscount
    guess_strings = list(raw_input("Enter your guess. \n"))
    guess = [int(guess_strings[i]) for i in range(len(guess_strings))]
    bulls = [guess[i] for i in [i for i in range(len(guess_strings)) if guess[i] == secret[i]]]
    cows = [x for x in guess if x in secret and (not(x in bulls))]
    bullnumber = len(bulls)
    cownumber = len(cows)
    print "bulls: " + str(bullnumber)
    print "cows: " + str(cownumber)#
    guesscount += 1

number_of_guesses = int(raw_input("Enter the number of guesses the codebreaker shall have. \n"))    
digits = int(raw_input("Choose digits \n"))
choices = int(raw_input("Choose choices (at least the number of digits) \n")) 

secret = choosenumber(digits, choices)
guesscount = 0
guess = []
while guess != secret and guesscount <= number_of_guesses:
    bulls_and_cows()
    
if guess == secret:
     print "Congratulations, you win!"

else:
    print "Sorry, you lose."
    print "The number was: " 
    print secret
    

       

        


            
