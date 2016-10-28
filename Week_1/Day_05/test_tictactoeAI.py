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
            square.set('_')
        self.assertFalse(board.board_full())
        for square in board.squares:
            square.set('O')
        self.assertTrue(board.board_full())
        for square in board.squares:
            square.set('_')
        for square in board.squares:
            square.set(choice(['X', 'O']))
        self.assertTrue(board.board_full())
        
class VictoryTestCase(unittest.TestCase): 
    def runTest(self):  
        board = tictactoeAI.TTTBoard(3,3)              
        self.assertFalse(board.victory("X"))
        self.assertFalse(board.victory("O"))
        for col_index in range(3):
            square = board.get_square(0, col_index)
            square.set("X")
        self.assertTrue(board.victory("X"))  
        board = tictactoeAI.TTTBoard(3,3)
        for col_index in range(3):
            square = board.get_square(0, col_index)
            square.set("O")
        self.assertTrue(board.victory("O"))
        board = tictactoeAI.TTTBoard(3,3)
        for index in range(3):
            square = board.get_square(index, index)
            square.set("X")  
        self.assertTrue(board.victory("X"))
        
class ForkTestCase(unittest.TestCase):
    def runTest(self):
        board = tictactoeAI.TTTBoard(3,3)
        board.get_square(0,0).set("X")
        board.get_square(1,0).set("X")
        board.get_square(0,1).set("X")
        self.assertTrue(board.fork_at(board.get_square(0,0), "X"))
        self.assertFalse(board.fork_at(board.get_square(0,0), "O"))
        board = tictactoeAI.TTTBoard(3,3)
        self.assertFalse(board.fork_at(board.get_square(0,0), "O"))
        board.get_square(0,0).set("O")
        board.get_square(1,1).set("O")
        board.get_square(0,2).set("O")
        self.assertTrue(board.fork_at(board.get_square(1,1), "O"))

class SeekWinTestCase(unittest.TestCase):
    def runTest(self):
        board = tictactoeAI.TTTBoard(3,3)
        board.get_square(0,0).set("X")
        board.get_square(1,0).set("X")
        self.assertEqual(board.seek_win("X"), board.get_square(2,0))    
        
      
        
class DisplayTestCase(unittest.TestCase):
    def runTest(self):
        board = tictactoeAI.TTTBoard(3,3)
        self.assertEqual(board.display_row(0), "_ _ _")
        # print " "
        # print board.display()
        self.assertEqual(board.display(), "_ _ _\n_ _ _\n_ _ _")
        
        
                
    
        
                    
        

if __name__ == '__main__':
    unittest.main()