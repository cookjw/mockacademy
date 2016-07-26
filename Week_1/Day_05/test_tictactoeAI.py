import unittest
import tictactoeAI
from random import choice

class BoardFullTestCase(unittest.TestCase): # passes
    def runTest(self):      
        board1 = tictactoeAI.TTTBoard(3,3)
        board = board1        
        for square in board.squares:
            square.set('X') 
        self.assertTrue(board.board_full()) 
        for square in board.squares:
            square.set('')
        self.assertFalse(board.board_full())
        for square in board.squares:
            square.set('O')
        self.assertTrue(board.board_full())
        for square in board.squares:
            square.set('')
        for square in board.squares:
            square.set(choice(['X', 'O']))
        self.assertTrue(board.board_full())
        
class VictoryTestCase(unittest.TestCase): # does not pass
    def runTest(self):  
        board2 = tictactoeAI.TTTBoard(3,3)
        board = board2
        print len(board.squares)
        self.assertFalse(board.victory("X"))
        self.assertFalse(board.victory("O"))
        # for col_index in range(3):
            # square = board.get_square(0, col_index)
            # square.set("X")
        # self.assertTrue(board.victory("X"))    
    
        
                    
        

if __name__ == '__main__':
    unittest.main()