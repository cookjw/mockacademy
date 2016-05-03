# Tic-Tac-Toe for human vs. computer


# CURRENT STATUS: Starting over (this is, after all, what version control is for).


class TTTSquare:
    def __init__(self, row, column):
	    self.value = ""
		self.row = row
		self.column = column


class TTTBoard:
    def __init__(self, rows, columns):
	    self.rows = rows
		self.columns = columns
		self.squares = []
		for row in range(rows):
		    for column in range(columns):
			    square = TTTSquare(row, column)
				self.squares.append(square)
				
    def get_square(row, column):
	    results = []
		for square in self.squares:
		    if square.row == row and square.column == column:
			    results.append(square)
		if len(results) == 1:
		    return results[0]
		else:
		    raise Exception("Yikes! More than one square with the same coordinates!")
	
	def board_full(self):
	    """
	    checks whether board is full
	    """
	    for square in self.squares:
		    if square.value == ""
			    return False
		return True
				
	def victory(self, symbol):
	    """
		checks whether a player ("symbol") has won
		"""
	    self.check_rows(symbol)
		self.check_columns(symbol)
		self.check_diagonals(symbol)
		
	def check_rows(self, symbol):	    
	    for row in range(self.rows):
            answer = True
            # reset to True each time			
		    for column in range(self, columns):
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
		for column in range(self.columns):
		    answer = True
		    for row in range(self, rows):
			    square = self.get_square(row, column)
				if square.value != symbol:
				    answer = False
				    break
            if answer == True:
                break
        return answer

    def check_diagonals(self, symbol):
	    answer = True
        row = 0
		column = 0		
		while row <= self.rows:
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
		    row = self.rows
		    column = 0
		    while row >= 0:			    
        	    square = self.get_square(row, column)	
			    if square.value != symbol:
			        answer = False
				    break
			    row -= 1
			    column += 1
			return answer
				
			
				
				
		    
		    
			 
				
		
		
		

    


