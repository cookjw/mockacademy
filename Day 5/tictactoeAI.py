# Tic-Tac-Toe for human vs. computer

# CURRENT STATUS: Unfinished (displays board).


class TicTacToe:

    def __init__(self, rows, columns, number, humanplayer):
        self.board = Board(rows, columns)
        self.number = number
        self.humanplayer = humanplayer
        if self.humanplayer == "X":
            self.computerplayer = "O"
        if self.humanplayer == "O":
            self.computerplayer = "X"
            
    def X_wins(self):
        pass
    
    def O_wins(self):
        pass
    
    def boardfull(self):
        for square in self.board.state:
            if self.board.state[square] == "_":
                return False
        return True
    
    def play(self):         
        self.board.displayboard()
        print self.boardfull()        
        
        
class Board:

    def __init__(self, rows, columns):
        state = {}
        for row in range(rows):
            for column in range(columns):
                state[(row, column)] = "_"
        self.state = state
        self.rows = rows
        self.columns = columns    


    def displayboard(self):        
        for row in range(self.rows):
            printcoord = ""
            for column in range(self.columns):
                printcoord = printcoord + " " + str(self.state[(row, column)]) 
            print printcoord        

    
    
    
    
game = TicTacToe(3,3,3,"X")    
game.play()    
        