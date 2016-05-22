import unittest
import tictactoeAI

class BoardFullTestCase(unittest.TestCase):
    def runTest(self):	    
        board = tictactoeAI.TTTBoard()	
 	    #the line below this comment produces an IndentationError! wtf
	    for square in board.squares:
		    square.set('X') 
		self.assertTrue(board.board_full())	

if __name__ == '__main__':
    unittest.main()