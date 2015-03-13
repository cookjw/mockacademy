# Tic-Tac-Toe for human vs. computer

# CURRENT STATUS: Unfinished (displays board and tests end conditions).


def next(coordinates, direction):
    if direction == "horizontal":
        return (coordinates[0], coordinates[1]+1)
    if direction == "vertical":
        return (coordinates[0]+1, coordinates[1])
    if direction == "diagonal":
        return (coordinates[0]+1, coordinates[1]+1)


class TicTacToe:

    def __init__(self, rows, columns, number, humanplayer):
        self.board = Board(rows, columns, number)
        self.rows = rows
        self.columns = columns
        self.number = number
        self.humanplayer = humanplayer
        if self.humanplayer == "X":
            self.computerplayer = "O"
        if self.humanplayer == "O":
            self.computerplayer = "X"    

    
    def play(self):    
        while not (self.board.wins("X") or self.board.wins("O")) and not self.board.full():        
            self.board.displayboard()  
            horiz = int(raw_input("Enter row number, starting from top: \n")) - 1
            vert = int(raw_input("Enter column number, starting from left: \n")) - 1
            symbol = raw_input("Enter symbol: \n")
            self.board.state[(horiz, vert)] = symbol
        for symbol in ["X", "O"]:
            if self.board.wins(symbol):
                self.board.displayboard()
                print symbol + " " + "wins!"
        if self.board.full():
            self.board.displayboard()
            print "Board Full!"
                        
        
        
class Board:

    def __init__(self, rows, columns, number, symbol="X"):
        state = {}
        for row in range(rows):
            for column in range(columns):
                state[(row, column)] = "_"
        self.state = state
        self.rows = rows
        self.columns = columns  
        self.number = number 
        self.symbol = symbol        


    def displayboard(self):        
        for row in range(self.rows):
            printcoord = ""
            for column in range(self.columns):
                printcoord = printcoord + " " + str(self.state[(row, column)]) 
            print printcoord  
            
    def full(self):
        for square in self.state:
            if self.state[square] == "_":
                return False
        return True

    def wins(self, symbol):    
        directions = ["horizontal", "vertical", "diagonal"]
        for direction in directions:        
            for square in self.state:            
                currentsquare = square
                in_a_row = 0            
                while currentsquare in self.state and self.state[currentsquare] == symbol:
                    in_a_row += 1
                    currentsquare = next(currentsquare, direction)
                if in_a_row >= self.number:
                    return True
        return False              

    
    
    
    
game = TicTacToe(3,3,3,"X")    
game.play()    
        