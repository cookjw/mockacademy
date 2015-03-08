from copy import copy


# A classic game of tic-tac-toe.
class TicTacToeGame():
    
    def __init__(self):
        self.setup()
        self.play()
        

    # This dict maps a turn index to the corresponding player's mark.
    turn_to_mark = {0:'X', 1:'O'}
    
    # This dict maps a player's mark to the corresponding turn index.
    mark_to_turn = {'X':0, 'O': 1}
    
    # Sets up the game.
    def setup(self):
        self.board = TicTacToeBoard()
        self.game_over = False
        
        # player objects are stored in the two-element list self.players
        self.players = []
        # self.turn indicates whose turn it is and indexes into @players
        self.turn = 0        
        
        human_players = None
        while not human_players:
            human_players = raw_input("How many human players?\n")
            if human_players == "0":
                self.players.append(ComputerTicTacToePlayer('X', 0))
                self.players.append(ComputerTicTacToePlayer('O', 1))
            elif human_players == "1":
                self.players.append(HumanTicTacToePlayer('X', 0))
                self.players.append(ComputerTicTacToePlayer('O', 1))
            elif human_players == "2":
                self.players.append(HumanTicTacToePlayer('X', 0))
                self.players.append(HumanTicTacToePlayer('O', 1))
            else:
                print "I'm sorry, I didn't understand that. Please enter '0', '1', or '2'. "
                human_players = None
                
        # Play!
        def play(self):
            while not self.game_over:
                # display the board
                self.board.show()
                
                # take a move
                move = self.players[self.turn].take_move(self.board)
                
                while not self.board.legal_move(move):
                    print "That move is not legal; try again!"
                    move = self.players[self.turn].take_move(self.board)
                    
                # mark the board
                self.board.mark(move, TicTacToeGame.turn_to_mark[self.turn])
                
                # evaluate the board, declare outcome as appopriate
                result = self.board.evaluate()
                if result:
                    self.game_over = True
                    self.board.show()
                    if result == 0: # first player win
                        print "Player 1 ('X') wins!"
                        print "Player 2 ('O') has been utterly defeated."
                        return 0
                    elif result == 1: # second player win
                        print "Player 2 ('O') wins!"
                        print "Player 1 ('X') has been utterly defeated."
                        return 1
                    elif result == 2: # tie
                        print "The game was a tie, a 'cat's game.'"
                        return 2
                        
                # Now it's the other player's turn---
                self.turn = (self.turn + 1) % 2
                
# The tic-tac-toe arena.
class TicTacToeBoard:
    
    # Creates the board (empty by default).
    def __init__(self, state = [['_' for _ in range(1, 4)] for _ in range(1,4)]):
        self.state = state
    
    # Returns the mark at indices i, j.
    def at(self, i, j):
        self.state[i][j]
        
    # Marks the board: +move+ is a two-element array, +mark+ is the
    # player's mark
    def mark(self, move, mark):
        self.state[move[0]][move[1]] = mark
         
    # Displays the board.
    def show(self):
        print 
        for row in self.state:
            for mark in row:
                print mark, ' '
            print "\n"
        print 
        
    # Overrides +#clone+ to give deep duplication.
    # (Probably highly unnecessary given the existence of copy.deepcopy)
    def clone(self):
        original_state = self.state
        copied_state = 
          
        

                    
                
                
                
                
                
                
                