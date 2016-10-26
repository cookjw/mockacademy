# Tic-Tac-Toe for human vs. computer

# CURRENT STATUS: Human vs. human interface seems to work.


class TTTSquare:
    def __init__(self, row, column):
        self.value = "_"
        self.row = row
        self.column = column
        
    def set(self, value):             
        self.value = value

        self.check_value()
    
    def check_value(self):
        if not self.value in ["_", "X", "O"]:
            raise Exception("Square value not valid!")
        


class TTTBoard:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.squares = []
        for row in range(rows):
            for column in range(columns):
                square = TTTSquare(row, column)
                self.squares.append(square)
     
    def display_row(self, row):
        row_string = self.get_square(row, 0).value
        for col in range(1, self.columns):
            row_string += " " + self.get_square(row, col).value
        return row_string
                
    def display(self):
        display_string = self.display_row(0)
        for row in range(1, self.rows):
            display_string += "\n" + self.display_row(row)       
        return display_string

            
                
    def get_square(self, row, column): #squares are zero-indexed!
        results = []
        for square in self.squares:
            if square.row == row and square.column == column:
                results.append(square)
        if len(results) <= 1:
            return results[0]
        else:
            raise Exception(
            "Yikes! More than one square with the same coordinates!"
            )
    
    def board_full(self):
        """
        checks whether board is full
        """
        for square in self.squares:
            if square.value == "_":
                return False
        return True
                
    def victory(self, symbol):
        """
        checks whether a player ("symbol") has won
        """
        if self.check_rows(symbol):
            return True
        elif self.check_columns(symbol):
            return True
        elif self.check_diagonals(symbol):
            return True
        else:
            return False
        
    def check_rows(self, symbol):   
        """
        (used by victory) checks whether a player has won in the 
        horizontal direction
        """     
        for row in range(self.rows):
            answer = True
            # reset to True each time            
            for column in range(self.columns):
                square = self.get_square(row, column)
                if square.value != symbol:
                    answer = False
                    break
                    #stop checking this row and move to next row
            if answer == True:
            # i.e. only values in row equal to target, 
            #i.e., victory condition
                break
                #don't go on to check additional rows
        return answer
        
    def check_columns(self, symbol):  
        """
        (used by victory) checks whether a player has won in the 
        vertical direction
        """     
        for column in range(self.columns):
            answer = True
            for row in range(self.rows):
                square = self.get_square(row, column)
                if square.value != symbol:
                    answer = False
                    break
            if answer == True:
                break
        return answer

    def check_diagonals(self, symbol):
        """
        (used by victory) checks whether a player has won in a diagonal
        """
        answer = True
        row = 0
        column = 0        
        while row < self.rows:
            square = self.get_square(row, column)
            if square.value != symbol:
                answer = False
                break
            row += 1
            column = row
        if answer:
            return answer        
        else:    
            answer = True
            row = self.rows - 1
            column = 0
            while row >= 0:                
                square = self.get_square(row, column)    
                if square.value != symbol:
                    answer = False
                    break
                row -= 1
                column += 1
            return answer
                
            
class TTTGame:
    def __init__(
    self, rows, columns, first_player="X", computer_players=()
    ):
        self.board = TTTBoard(rows, columns)
        self.first_player = first_player
        for item in computer_players:
            if not item in ("X", "O"):
                raise Exception("invalid computer player!")
        self.computer_players = computer_players
        
    def switch_turn(self):
        if self.player == "X":
            self.player = "O"
        elif self.player == "O":
            self.player = "X"
            
    def get_square_from_player(self, player): 
        #will need dependence on nature of player later
        if player in self.computer_players:
            pass #do AI magic
        else:
            allowable_row_inputs = [
            str(x) for x in range(self.board.rows)
            ]
            allowable_column_inputs = [
            str(x) for x in range(self.board.columns)
            ]        
            row_input = raw_input(
            "Enter row coordinate for {}: ".format(self.player)
            )            
            while not row_input in allowable_row_inputs:
                print "Invalid row input. Please try again."
                row_input = raw_input(
                "Enter row coordinate for {}: ".format(self.player)
                )
            row_coordinate = int(row_input)
            column_input = raw_input(
            "Enter column coordinate for {}: ".format(self.player)
            )
            while not column_input in allowable_column_inputs:
                print "Invalid column input. Please try again. "
                column_input = raw_input(
                "Enter column coordinate for {}: ".format(self.player)
                )            
            column_coordinate = int(column_input)
            return self.board.get_square(
            row_coordinate, column_coordinate
            )
    
    def play(self):  
        print self.board.display()
        self.player = self.first_player    
        while (
        not self.board.victory("X") and not self.board.victory("O")
        and not self.board.board_full()):
            square = self.get_square_from_player(self.player)
            while square.value != "_":
                print "Square already occupied!"   
                square = self.get_square_from_player(self.player)                
            square.set(self.player)                
            self.switch_turn()
            print self.board.display()
        if self.board.victory("X"):
            print "X wins!"
        elif self.board.victory("O"):
            print "O wins!"
        elif self.board.board_full():
            print "Board full!"
        else:
            print "We're out of the loop and I don't know why."
            
            
        

        
 
if __name__ == "__main__":
    game = TTTGame(3,3)
    game.play()
          
            
            
             
                
        
        
        

    


