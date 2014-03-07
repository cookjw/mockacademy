#Translation of Hangman by Zack Davis and Jen Hamon, App Academy Week 1
#Original at https://github.com/zackmdavis/App_Academy_Exercises/blob/master/Week_1/hangman.rb

#CURRENT STATUS: ComputerHangman + HumanCondemned working ok, as in original. HumanHangman + ComputerCondemned broken in original, but other errors in this version.

import random
import string
import re
import collections

class HangmanGame:
    def __init__(self):
        self.stickman = Stickman()
        self.rejected_guesses = []
        # print "self.rejected_guesses: {} ".format(' '.join(self.rejected_guesses))
        self.setup()
        # print "Hi"
        # print self.rejected_guesses
        self.play()
    
    
    def setup(self):
        humans = int(raw_input("How many human players?\n"))
        if humans == 1:
            player_role = int(raw_input("Would you like to be the 1) hangman or the 2) condemned?\n"))
            if player_role == 1:
                self.hangman = HumanHangman()
                self.condemned = ComputerCondemned()
            else:
                self.hangman = ComputerHangman()
                self.condemned = HumanCondemned()
        elif humans == 2:
            self.hangman = HumanHangman()
            self.condemned = HumanCondemned()
        else:
            self.hangman = ComputerHangman()
            self.condemned = ComputerCondemned()
        self.hangman.make_secret()
        self.revealed = '_ '*self.hangman.secret_length        
        
                
    
    def play(self):
        while self.stickman.still_alive() and '_' in self.revealed:
            self.stickman.display()
            print self.revealed
            # print self.rejected_guesses              
            print "failed guesses: {}".format(' '.join(self.rejected_guesses))           
            guess = self.condemned.guess(self.revealed)
            locations = self.hangman.check(guess) # list of indices where guess appears
            if len(locations) == 0:
                self.stickman.add_part()
                self.rejected_guesses.append(guess)
            else:
                revealed_list = list(self.revealed)
                for i in locations:
                    revealed_list[i] = guess
                self.revealed = ''.join(revealed_list)    
        if self.stickman.still_alive():
            print     "The word has been guessed; the prisoner shall live another day"
        else:
            self.stickman.display()
            print "The word was not guessed; the prisoner is dead" 
            # print self.hangman.secret            
    
    
class Stickman:
  #  |--|
  #  0  |
  # /T\ |
  # / \ |
  # ____|
    
    def __init__(self):
        self.parts = [['O',1,1],['T',2,1], ['/', 2, 0], ["\\", 2, 2], ['/', 3, 0], ["\\", 3, 2]]
        self.illustration = [[' ', '|', '-', '-', '|'],
                     [' ', ' ', ' ', ' ', '|'],
                     [' ', ' ', ' ', ' ', '|'],
                     [' ', ' ', ' ', ' ', '|'],
                     ['_', '_', '_', '_', '|']]
                     
    
    def add_part(self):
        part, i, j = self.parts.pop(0)
        self.illustration[i][j] = part
    
    def display(self):
        for line in self.illustration:
             print ''.join(line)
        print
    
    def still_alive(self):
        return len(self.parts) != 0
        
        
class HumanHangman:
    def make_secret(self):
        print "Come up with a secret word!"
        self.secret_length = int(raw_input("What length is your secret word?\n"))
        
    def check(self,guess):
        print "The guess was the letter {}".format(guess)
        input = raw_input("Input indices at which this letter appears in the secret word, separated by only commas\n")
        return [int(c) - 1 for c in input.split(',')]
        
        
class ComputerHangman:
    def make_secret(self):
        self.secret = random.choice(open('dictionary.txt').readlines())[:-1].upper()
        if '-' in self.secret:
            self.make_secret()
        self.secret_length = len(self.secret)       
    
    
    def check(self, guess):
        locations = []
        for i, letter in list(enumerate(self.secret)):
            if letter == guess:
                locations.append(i)
        # print "locations: {}".format(locations)
        return locations
    
    
class HumanCondemned:
    def guess(self, revealed):
        return raw_input("Guess a letter: \n").upper()
        
 
 
class ComputerCondemned:
    def __init__(self):
        self.previous_guesses = []
        self.words = [x[:-1].upper() for x in open('dictionary.txt').readlines()]
     
    def dumb_guess(self):
        attempt = random.choice(string.asci_letters)
        while attempt in self.previous_guesses:
            attempt = random.choice(string.asci_letters)            
        self.previous_guesses.append(attempt)
        return attempt        
        
     
    def guess(self, revealed):
        rejected_letters = self.__infer_rejected_letters(revealed)
        self.__update_words(revealed, rejected_letters)
        all_letters = [letter for letter in list(('').join(self.words)) if not (letter in self.previous_guesses)]
        letter_frequencies = collections.defaultdict(int)
        for chr in all_letters:
            letter_frequencies[chr] += 1
        next_guess = sorted(letter_frequencies, key=letter_frequencies.get())[-1]
        self.previous_guesses.append(next_guess)
        return next_guess
     
    def __infer_rejected_letters(self, revealed):
        return [letter for letter in self.previous_guesses if not (letter in revealed)]
     
    def __pattern_match(self, word, matcher):
        match = re.search(matcher, word)
        if match:
            return True
        else:
            return False
     
    def __update_words(self, revealed, rejected_letters):
         matcher = '\A' + re.sub('_', '\w', revealed) + '\Z'
         self.words = [word for word in self.words if self.__pattern_match(word, matcher) and [l for l in word if l in rejected_letters] == []]
         
         
         
game = HangmanGame()
        