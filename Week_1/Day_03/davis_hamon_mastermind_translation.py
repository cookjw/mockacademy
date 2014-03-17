#Python translation of Mastermind by Zack Davis and Jen Hamon, App Academy Week 1
#Original at https://github.com/zackmdavis/App_Academy_Exercises/blob/master/Week_1/mastermind.rb

import time
import random

class MastermindGame:
    def __init__(self, pegs, guesses):
        self.pegs = pegs
        self.guesses = guesses
        self.previous_results = []
        self.last_guess = None
        self.last_result = None
        self.guesser = GuessingPlayer()
        self.master = MasterPlayer(pegs, 'ROYGBIV')
        self.game_over = False
        
    def play(self):
        while not self.game_over:
           self.__display_previous_guesses()
           self.last_guess = self.guesser.make_guess()
           self.last_result = self.master.check(self.last_guess)
           # print self.last_result
           self.previous_results.append([self.last_guess, self.last_result])
           if self.__guesser_win():
               # print self.pegs
               # print self.last_result["exact"]
               # print self.__guesser_win()
               # print self.__guesser_win
               self.__win_message()
           if self.__out_of_guesses():
               self.__lose_message()
           
               
    
    def __display_previous_guesses(self):
        for result in self.previous_results:
            print (' ').join(result[0]) + " | %(exact)s %(color_only)s " % {'exact' : result[1]["exact"], 'color_only': result[1]["color_only"]}
        print ''
    
    def __win_message(self):
        print "You guessed my secret!! You win."
        self.game_over = True
    
    def __lose_message(self):
        print "You've taken too long. The secret is mine forever!!!!!!!!!"
        time.sleep(1)
        print "..."
        time.sleep(1)
        print "No, I guess you deserve to know, after all"
        secret = ''.join(self.master.secret)
        print "The secret is %s" % secret
        self.game_over = True
    
    def __guesser_win(self):
        return self.last_result["exact"] == self.pegs
    
    def __out_of_guesses(self):
        return len(self.previous_results) == self.guesses

class GuessingPlayer:
    def __init__(self):
        pass
    
    def make_guess(self):        
        guess = list(raw_input("Enter your guess!\n").upper())
        return guess

class MasterPlayer:
    def __init__(self, num_pegs, colors):
        self.number_of_pegs = num_pegs
        self.colors = colors
        self.secret = self.invent_secret()
                
        
    def invent_secret(self):
        secret = []
        for n in range(self.number_of_pegs):
            secret.append(self.colors[random.randrange(0,len(self.colors))])
        return secret    
    
    def check(self, guess):
        exact_indices = self.__check_exact(guess)
        color_only = self.__check_color_only(guess, exact_indices)
        result = {"exact": len(exact_indices), "color_only": color_only}
        # print result
        return result
        
        
    def __check_exact(self, guess):
        exact_indices = []
        for i, guess_el in enumerate(guess):
            if guess_el == self.secret[i]:
                exact_indices.append(i)
                # print exact_indices
        # print exact_indices
        return exact_indices
    
    def __check_color_only(self, guess, exact_indices):
        nonexact_indices = [i for i in range(self.number_of_pegs) if not (i in exact_indices)]
        # print nonexact_indices
        unmatched_secret = [self.secret[i] for i in nonexact_indices]
        # print unmatched_secret
        unmatched_guess = [guess[i] for i in nonexact_indices]
        color_matches = 0
        for guess_peg in unmatched_guess:
            if guess_peg in unmatched_secret:
                color_matches += 1
                del unmatched_secret[unmatched_secret.index(guess_peg)]
        # print color_matches
        return color_matches
            
    

if __name__ == "__main__":
    game = MastermindGame(4,12)
    game.play()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    