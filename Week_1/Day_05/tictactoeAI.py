# Tic-Tac-Toe for human vs. computer

# CURRENT STATUS: play appears to work.




def check_empty_segment(segment):
    for square in segment:
        if square.value != "_":
            return False
    return True

def get_empty_square(segment):
    for square in segment:
        if square.value == "_":
            return square        
        


class TTTSquare:
    def __init__(self, row, column):
        self.value = "_"
        self.row = row
        self.column = column
        
    def __repr__(self):
        return "square ({}, {})".format(
        str(self.row), str(self.column)
        )
        
    def set(self, value):             
        self.value = value

        self.check_value()
    
    def check_value(self):
        if not self.value in ["_", "X", "O"]:
            raise Exception("Square value not valid!")
            
    def copy(self):
        new_copy = TTTSquare(self.row, self.column)
        new_copy.value = self.value
        return new_copy
            
        


class TTTBoard:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.squares = []
        
        for row in range(rows):
            for column in range(columns):
                square = TTTSquare(row, column)
                self.squares.append(square)
                
        self.positive_diagonal = [
        self.get_square(index, rows - index -1) for index in range(rows)
        ]
        self.negative_diagonal = [
        self.get_square(index,index) for index in range(rows)
        ]
        
        self.corner_squares = [
        self.get_square(0,0), self.get_square(self.rows - 1, 0),
        self.get_square(0, self.columns - 1), self.get_square(
        self.rows - 1, self.columns - 1)]
        
        self.top_side = [
        self.get_square(0, col) for col in range(self.columns - 1)
        ]
        self.bottom_side = [
        self.get_square(self.rows - 1, col) for col in range(
        self.columns - 1
        )
        ]
        self.left_side = [
        self.get_square(row, 0) for row in range(self.rows - 1)
        ]
        self.right_side = [
        self.get_square(
        row, self.columns - 1) for row in range(self.rows - 1)
        ]
        
        self.sides = [
        self.top_side, self.bottom_side, self.left_side, self.right_side
        ]
                
    def __str__(self):
        return self.display()
        
    def copy(self):
        new_copy = TTTBoard(self.rows, self.columns)
        new_copy.squares = []
        for square in self.squares:
            new_copy.squares.append(square.copy())
        return new_copy
     
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

    
    def segments(self, square):
        """
        returns [row, column, positive_diagonal, negative_diagonal], 
        where each item in the list is a list of squares representing
        a win-condition-relevant segment of the board containg the given
        square
        """
        row = [
        self.get_square(
        square.row, column
        ) for column in range(self.columns)
        ] 
        column = [
        self.get_square(
        owray, square.column
        ) for owray in range(self.rows)
        ]
        if square.row == square.column:
            negative_diagonal = self.negative_diagonal
        else:
            negative_diagonal = []
        if square.row + square.column == self.rows - 1:
            positive_diagonal = self.positive_diagonal
        else:
            positive_diagonal = []
        return [row, column, positive_diagonal, negative_diagonal]
        
    def fork_at(self, square, symbol):
        """
        checks whether a square participates in two simulatenous 
        win opportunities
        """        
        opportunity_count = 0
        # print "row: " + str(row)
        # print "column: " + str(column)
        for segment in self.segments(square):  
            # print segment        
            opportunity = 0
            for location in segment:
                if location.value == self.get_opponent(symbol):
                    break
                elif location.value == symbol:
                    opportunity += 1
                elif location.value == "_":
                    continue
                else:
                    raise Exception("Something went wrong!")
            # print "opportunity: " + str(opportunity)
            if opportunity >= self.rows - 1:
                opportunity_count += 1        
        if opportunity_count >= 2:
            # print "opportunity_count: " + str(opportunity_count)
            return True
        else:
            return False
                
    
    def seek_win(self, symbol):
        """
        Step 1 of the AI algorithm in Wikipedia
        """        
        for square in self.squares:
            if square.value == "_":
                hypothetical_board = self.copy()
                hypothetical_board.get_square(
                square.row, square.column
                ).set(symbol)                
                if hypothetical_board.victory(symbol):
                    return square        
        
    def seek_block(self, symbol):
        """
        Step 2 of the AI algorithm in Wikipedia
        """
        opponent = self.get_opponent(symbol)
        return self.seek_win(opponent)             

        
    def seek_fork(self, symbol):
        """
        Step 3 of the AI algorithm in Wikipedia
        """
        for square in self.squares:
            if square.value == "_":
                # print square
                hypothetical_board = self.copy()
                h_square = hypothetical_board.get_square(
                square.row, square.column
                )
                h_square.set(symbol)
                # print hypothetical_board
                if hypothetical_board.fork_at(h_square, symbol):
                    return square        
                # else:
                    # print "no fork at: " + str(square)                
            
        
    def seek_blockfork_1(self, symbol):
        """
        Step 4, Option 1 of the AI algorithm in Wikipedia
        """

        player = symbol
        opponent = self.get_opponent(player)
        #Obviously this suggests that seek_blockfork_2 should be first: 
        if not self.seek_blockfork_2(player):         
            for square in self.squares:
                for segment in self.segments(square):
                    selfcount = 0
                    oppcount = 0
                    for aresquay in segment:
                        if aresquay.value == opponent:
                            oppcount += 1
                            break
                        if aresquay.value == player:
                            selfcount += 1
                    if selfcount == self.rows - 2 and oppcount == 0:
                        return get_empty_square(segment)                    
            
            

        
    def seek_blockfork_2(self, symbol):
        """
        Step 4, Option 2 of the AI algorithm in Wikipedia
        """
        opponent = self.get_opponent(symbol)

        return self.seek_fork(opponent)         

        
    def get_center(self):
        """
        Step 5 of the AI algorithm in Wikipedia
        """
        if self.rows == self.columns and self.rows % 2 == 1:
            return self.get_square(self.rows/2, self.columns/2)
        else:
            pass
            
    def opposite_corner(self, corner_square):
        rows = self.rows - 1
        columns = self.columns - 1
        if (corner_square.row, corner_square.column) == (rows,0):        
            return self.get_square(0, rows)
        elif (corner_square.row, corner_square.column) == (0, columns):
            return self.get_square(columns, 0)  
        elif (corner_square.row, corner_square.column) == (0,0):
            return self.get_square(rows, columns)
        elif (corner_square.row, corner_square.column) == (rows, columns):
            return self.get_square(0,0)
        else:
            raise Exception("Not a corner square!")
                    
    
    def seek_opposite_corner(self, symbol):
        """
        Step 6 of the AI algorithm in Wikipedia
        """
        opponent = self.get_opponent(symbol)
        for corner_square in self.corner_squares:
            if (corner_square.value == opponent and
            self.opposite_corner(corner_square).value == "_"):
                return self.opposite_corner(corner_square)       
        
    def seek_empty_corner(self):
        """
        Step 7 of the AI algorithm in Wikipedia
        """
        for corner_square in self.corner_squares:
            if corner_square.value == "_":
                return corner_square
        
    def seek_empty_side(self):
        """
        Step 8 of the AI algorithm in Wikipedia
        """
        def halfway_index(my_list):
            return len(my_list)/2
        for segment in self.sides:
            if check_empty_segment(segment):
                return segment[halfway_index(segment)]            
        
        
    def get_opponent(self, symbol):
        player = symbol
        if player == "X":
            opponent = "O"
        elif player == "O":
            opponent = "X"
        else:
            raise Exception("invalid player symbol")
        return opponent
    
    def computer_move(self, symbol):
        """
        runs an AI program to compute optimal move
        """
        player = symbol
        winning_move = self.seek_win(player)
        if winning_move:
            return winning_move
        blocking_move = self.seek_block(player)
        if blocking_move:
            return blocking_move
        forking_move = self.seek_fork(player)
        if forking_move:
            return forking_move
        blockfork_option_1 = self.seek_blockfork_1(player)
        if blockfork_option_1:
            return blockfork_option_1
        blockfork_option_2 = self.seek_blockfork_2(player)
        if blockfork_option_2:
            return blockfork_option_2
        center = self.get_center()
        if center.value == "_":
            return center
        opposite_corner = self.seek_opposite_corner(player)
        if opposite_corner:
            return opposite_corner 
        empty_corner = self.seek_empty_corner()
        if empty_corner:
            return empty_corner
        empty_side = self.seek_empty_side()
        if empty_side:
            return empty_side
        pass 
                
            
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
        if player in self.computer_players:
            return self.board.computer_move(player)
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
            print " "
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

    print "Welcome to Tic-Tac-Toe!"
    
    computer_players = []   
    
    gen_string = """
    Choose type of player for {}.
    (Type C for computer, H for human; then press ENTER.)
    """
    x_string = gen_string.format("X")
    o_string = gen_string.format("O")
    x_c_or_h = raw_input(x_string).upper()
    o_c_or_h = raw_input(o_string).upper()
    if x_c_or_h =="C":
        computer_players.append("X")
    if o_c_or_h == "C":
        computer_players.append("O")        
    computer_players = tuple(computer_players)    
    
    game = TTTGame(3,3, computer_players = computer_players)
    game.play()
          
            
            
             
                
        
        
        

    


