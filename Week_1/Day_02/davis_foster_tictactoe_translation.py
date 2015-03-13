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
                # print 
                move = self.players[self.turn].take_move(self.board)
                
            # mark the board
            self.board.mark(move, TicTacToeGame.turn_to_mark[self.turn])
            
            # evaluate the board, declare outcome as appopriate
            result = self.board.evaluate()
            print "result: " + str(result)
            if result in ['0','1','2']:
                print "result: " + str(result)
                self.game_over = True
                self.board.show()
                if result == '0': # first player win
                    print "Player 1 ('X') wins!"
                    print "Player 2 ('O') has been utterly defeated."
                    return '0'
                elif result == '1': # second player win
                    print "Player 2 ('O') wins!"
                    print "Player 1 ('X') has been utterly defeated."
                    return '1'
                elif result == '2': # tie
                    print "The game was a tie, a 'cat's game.'"
                    return '2'
                    
            # Now it's the other player's turn---
            self.turn = (self.turn + 1) % 2
                
# The tic-tac-toe arena.
class TicTacToeBoard:
    
    # Creates the board (empty by default).
    def __init__(self, state = None):
        if state is None:
            state = [['_' for _ in range(1, 4)] for _ in range(1,4)]
        self.state = state
    
    # Returns the mark at indices i, j.
    def at(self, i, j):
        return self.state[i][j]
        
    # Marks the board: +move+ is a two-element array, +mark+ is the
    # player's mark
    def mark(self, move, mark):
        self.state[move[0]][move[1]] = mark
         
    # Displays the board.
    def show(self):
        print 
        for row in self.state:
            rowchars = ""
            for mark in row:
                rowchars += mark + ' '
            print rowchars    
            print "\n"
        print 
        
    # Overrides +#clone+ to give deep duplication.
    # (Probably highly unnecessary given the existence of copy.deepcopy)
    def clone(self):
        original_state = self.state
        copied_state = [copy(original_state[row]) for row in range(3)]
        return TicTacToeBoard(copied_state)
        
    # Return true if the supplied move is legal.
    def legal_move(self, move):
        # print self.at(move[0], move[1])
        return self.at(move[0], move[1]) == '_'
        
    # Returns an array of all legal moves.
    def legal_moves(self):
        all_moves = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0],
            [2,1], [2,2]]
        x = [move for move in all_moves if self.at(move[0], move[1]) == '_']
        # assert x != []
        # print x
        return x
        
        
    # Returns an array of possible next boards given mark of player to
    # move next.
    def possible_next_boards(self, mark):
        possible_moves = self.legal_moves()
        possible_boards = []
        for possible_move in possible_moves:
            next_board = self.clone()
            next_board.mark(possible_move, mark)
            possible_boards.append(next_board)
        return possible_boards
    
    # Returns 0, 1, 2, or False for first player win, second player win,
    # tie, and game-not-over-yet, respectively.
    def evaluate(self):
        line_results = [TicTacToeBoard.evaluate_line(l) for l in self.lines()]
        # print "line_results: " + str(line_results)
        line_results = [x for x in line_results if x is not False]
        if line_results != []: # win
            # print "a winning condition has occurred"
            # print "line_results: " + str(line_results)
            return [result for result in line_results][0]
        elif not self.legal_moves(): # tie
            return '2'
        else: # keep playing
            # print "no end condition yet"
            return False
            
    # Returns a move location at which supplied +current+ and +target+
    # boards are different.
    @classmethod
    def move_to_achieve_state(cls, current, target):
        for row in range(3):
            for col in range(3):
                if current.at(row, col) != target.at(row, col):
                    return [row, col]
    
    # Returns 0 (respectively 1) if the supplied array of marks
    # indicates a win for the first (respectively second) player.
    @classmethod
    def evaluate_line(cls, line):
        print "evaluating: " + ''.join(line)
        if ''.join(line) == 'XXX':
            return '0'
        elif ''.join(line) == 'OOO':
            return '1'
        else:
            print 'diff: ' + ''.join(line) + 'XXX'
            return False
        
    # Returns array of marks for all rows, diagonals, and columns.
    def lines(self):
        all_lines = []
        for row in range(3): # check rows
            all_lines.append([self.at(row, col) for col in range(3)])
        for col in range(3): # check columns
            all_lines.append([self.at(row, col) for col in range(3)])     
        # check diagonals
        all_lines.append([self.at(i,i) for i in range(3)])
        all_lines.append([self.at(i, 2-1) for i in range(3)])
        return all_lines
        
# This class represents a human player.
class HumanTicTacToePlayer:
    
    def __init__(self, mark, turn):
        self.mark = mark
        
    # Records the human's move.
    def take_move(self, board):
        input = raw_input("Human player, enter your move like 'row, column'\n")
        return [int(chr) for chr in input.split(',') if chr != ' ']
        
        
# This class represents a node in a game tree for use by AI players.
class GametreeNode:
    pass

# Currently under development!
class ComputerTicTacToePlayer:
    pass




if __name__ == '__main__':
    TicTacToeGame()

        
          
        

                    
                
                
                
                
                
                
                