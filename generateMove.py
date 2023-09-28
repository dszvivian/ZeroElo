import chess
import random
from evaluate import retBestCaptureMove



# Returns a first move on each type
def getFirstMove(board):
    for l in board.legal_moves:
        global a
        a = str(l)
        break
    return a 


# Returns CheckMates if Any
def getCheckmates(board:chess.Board):
    for l in board.legal_moves:
        localBoard = chess.Board(board.board_fen())
        localBoard.push(l)
        if(localBoard.is_checkmate()):
            return l
    return None



# Checks for Checkmates if any or else returns a random Move 
def getRandomMove(board):
    rNo = random.randrange(0,board.legal_moves.count())
    i = 0
    for l in board.legal_moves:

        global a
        if(i==rNo):
            a = l
            break
        i = i+1
    return a
    

def getBestCapture(board:chess.Board):
    #Calculate all the possible capturing Moves
    capturing_moves = []
    for l in board.legal_moves:
        if(board.is_capture(l)):
            capturing_moves.append(l)

    #Get the Best capture
    return retBestCaptureMove(board,capturing_moves)
          

def getBestMove(board:chess.Board):
    if(not getCheckmates(board)==None):#Check for Checkmates
        return getCheckmates(board)
    
    if(not getBestCapture(board)==None):
        return getBestCapture(board)

    else:
        getRandomMove(board)

