# Tic-Tac-Toe for human vs. computer

# CURRENT STATUS: Unfinished (displays board).


class TicTacToe:

    def __init__(self, rows, columns, humanplayer):
        self.gameboard = Board(rows, columns)
        self.humanplayer = humanplayer
        if self.humanplayer == "X":
            self.computerplayer = "O"
        if self.humanplayer == "O":
            self.computerplayer = "X"
    
    def play(self):         
        self.gameboard.displayboard()        
        
        
class Board:

    def __init__(self, rows, columns):
        board = {}
        for row in range(rows):
            for column in range(columns):
                board[(row, column)] = Square(row, column)
        self.board = board
        self.rows = rows
        self.columns = columns
    
    def boardstate(self):
        return {square : self.board[square].state for square in self.board}

    def displayboard(self):        
        for row in range(self.rows):
            printcoord = ""
            for column in range(self.columns):
                printcoord = printcoord + " " + str(self.board[(row, column)].state) 
            print printcoord        
            
                
                
                
class Square:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.state = "_"  
    
    
    
    
game = TicTacToe(3,3,"X")    
game.play()    
        