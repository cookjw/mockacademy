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
        self.board = Board(rows, columns)
        self.number = number
        self.humanplayer = humanplayer
        if self.humanplayer == "X":
            self.computerplayer = "O"
        if self.humanplayer == "O":
            self.computerplayer = "X"
    
    def wins(self, symbol):    
        directions = ["horizontal", "vertical", "diagonal"]
        for direction in directions:        
            for square in self.board.state:            
                currentsquare = square
                in_a_row = 0            
                while currentsquare in self.board.state and self.board.state[currentsquare] == symbol:
                    in_a_row += 1
                    # print (currentsquare[0]+1, currentsquare[1]+1) 
                    # print direction + " " + str(in_a_row)
                    currentsquare = next(currentsquare, direction)
                if in_a_row >= self.number:
                    return True
        return False                    

    def boardfull(self):
        for square in self.board.state:
            if self.board.state[square] == "_":
                return False
        return True
    
    def play(self):    
        while not (self.wins("X") or self.wins("O")) and not self.boardfull():        
            self.board.displayboard()
            print "X wins: " + str(self.wins("X"))
            print "O wins: " + str(self.wins("O"))
            print "board full: " + str(self.boardfull())  
            horiz = int(raw_input("Enter horizontal coordinate: \n")) - 1
            vert = int(raw_input("Enter vertical coordinate: \n")) - 1
            symbol = raw_input("Enter symbol: \n")
            self.board.state[(vert, horiz)] = symbol
        for symbol in ["X", "O"]:
            if self.wins(symbol):
                self.board.displayboard()
                print symbol + " " + "wins!"
        if self.boardfull():
            self.board.displayboard()
            print "Board Full!"
                        
        
        
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
        