#Tic-Tac-Toe for two players

#Remaining issues:
#    allows players to pass by entering coordinates of own square


board = {(0,0) : "_", (1,0) : "_", (2,0) : "_", (0,1) : "_", (1,1) : "_", (2,1) : "_", (0,2) : "_", (1,2) : "_", (2,2) : "_",}

def horizontalright(square):
    return ((square[0] + 1)%3, square[1])
    
def verticalup(square):
    return (square[0], (square[1] + 1)%3)
    
def diagonalright(square):
    return ((square[0] + 1)%3, (square[1] + 1)%3)
    
def diagonalleft(square):
    return ((square[0] - 1)%3, (square[1] + 1)%3)
    
    
def threeinarow(square):
    if (board[square] == board[horizontalright(square)] == board[horizontalright(horizontalright(square))] == "X") or \
    (board[square] == board[horizontalright(square)] == board[horizontalright(horizontalright(square))] == "O"):
        return True
    elif (board[square] == board[verticalup(square)] == board[verticalup(verticalup(square))] == "X") or \
    (board[square] == board[verticalup(square)] == board[verticalup(verticalup(square))] == "O"):
        return True
    elif square == (1,1) and((board[square] == board[diagonalright(square)] == board[diagonalright(diagonalright(square))] == "X") or \
    (board[square] == board[diagonalright(square)] == board[diagonalright(diagonalright(square))] == "O")):
        return True
    elif square == (1,1) and ((board[square] == board[diagonalleft(square)] == board[diagonalleft(diagonalleft(square))] == "X") or \
    (board[square] == board[diagonalleft(square)] == board[diagonalleft(diagonalleft(square))] == "O")):
        return True
    else:
        return False
        
def end_condition():
    status = True
    for square in board.keys():
        if threeinarow(square):
            status = True
            print "three in a row for " + str(square[0]+1) + " , " + str(square[1]+1)
            break
        elif board[square] == "_":
            status = False
    return status    
    
def printboard():
    print board[(0,2)] + " " + board[(1,2)] + " " + board[(2,2)]
    print board[(0,1)] + " " + board[(1,1)] + " " + board[(2,1)]
    print board[(0,0)] + " " + board[(1,0)] + " " + board[(2,0)]


 
while not end_condition():
    printboard()
    
    
    player1horiz = int(raw_input("Player 1 (X) enter horizontal coordinate(1, 2, or 3)\n")) - 1
    player1vert = int(raw_input("Player 1 (X) enter vertical coordinate(1, 2, or 3)\n")) - 1    
    player1square = (player1horiz, player1vert)
    while board[player1square] == "X":
        print "Sorry, square already occupied."
        player1horiz = int(raw_input("Player 1 (X) enter horizontal coordinate(1, 2, or 3)\n")) - 1
        player1vert = int(raw_input("Player 1 (X) enter vertical coordinate(1, 2, or 3)\n")) - 1    
        player1square = (player1horiz, player1vert)
    
    while board[player1square] != "X": 
        if board[player1square] == "_":             
            board[player1square] = "X"
        else:
            print "Sorry, square already occupied."
            player1horiz = int(raw_input("Player 1 (X) enter horizontal coordinate(1, 2, or 3)\n")) - 1
            player1vert = int(raw_input("Player 1 (X) enter vertical coordinate(1, 2, or 3)\n")) - 1    
            player1square = (player1horiz, player1vert)
    
    printboard()
    
    if end_condition():
        break
    
    player2horiz = int(raw_input("Player 2 (O) enter horizontal coordinate(1, 2, or 3)\n")) - 1
    player2vert = int(raw_input("Player 2 (O) enter vertical coordinate(1, 2, or 3)\n")) - 1
    player2square = (player2horiz, player2vert) 
    while board[player2square] == "O":
        print "Sorry, square already occupied."    
        player2horiz = int(raw_input("Player 2 (O) enter horizontal coordinate(1, 2, or 3)\n")) - 1
        player2vert = int(raw_input("Player 2 (O) enter vertical coordinate(1, 2, or 3)\n")) - 1
        player2square = (player2horiz, player2vert)  
    while board[player2square] != "O":    
        if board[player2square] == "_":    
            board[player2square] = "O"  
        else:
            print "Sorry, square already occupied."    
            player2horiz = int(raw_input("Player 2 (O) enter horizontal coordinate(1, 2, or 3)\n")) - 1
            player2vert = int(raw_input("Player 2 (O) enter vertical coordinate(1, 2, or 3)\n")) - 1
            player2square = (player2horiz, player2vert) 

printboard()
print "Game Over!"



     
