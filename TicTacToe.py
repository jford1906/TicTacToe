import numpy as np

#constructs a square array of the given size
def MakeBoard(size):
    return np.zeros((size,size),dtype=int)

#takes an integer and an array, plays a move in a non-empty space, returns the board and the location of the last move
def MakeMove(player, board):
    size = len(board)
    p1 = np.random.randint(size)
    p2 = np.random.randint(size)
    while board[p1,p2] != 0:
        p1 = np.random.randint(size)
        p2 = np.random.randint(size)
    board[p1,p2]=player
    return (board,p1,p2)

#Takes in a board and the location of the last move, and checks for a winner    
#def CheckWin(board, lastMove):
    #Where was the last move? What spots needs to be checked? Just write these out in words for each case, and we'll program it on Friday

    

#def PlayGame():
    #assign a variable to a board
    #pick a variable to indicate a win, and assign it the value "False"
    #set up a while loop until the win variable is true
        #make a move
        #check for a win
        #switch players
    
    



    
