# Tic-Tac-Toe for human vs. computer

# CURRENT STATUS: Starting over (this is, after all, what version control is for).


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

            
                
    def get_square(self, row, column):
        results = []
        for square in self.squares:
            if square.row == row and square.column == column:
                results.append(square)
        if len(results) <= 1:
            return results[0]
        else:
            raise Exception("Yikes! More than one square with the same coordinates!")
    
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
    def __init__(self, rows, columns, first_player="X"):
        self.board = TTTBoard(rows, columns)
        self.first_player = first_player
        
    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn == "X"
            
    def get_square_from_player(self, turn): 
        #will need dependence on player later
        pass
    
    def play(self):  
        self.turn = first_player    
        while (not self.victory("X") and not self.victory("O")
            and not self.board_full()):
            square = get_square_from_player(self.turn) 
            square.set(self.turn)
            self.switch_turn()
        
       
        
 
                
            
            
             
                
        
        
        

    


