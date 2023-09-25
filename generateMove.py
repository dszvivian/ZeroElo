import chess
import random




# Returns a first move on each type
def getFirstMove(board):
    for l in board.legal_moves:
        global a
        a = str(l)
        break
    return a 


# Returns CheckMates if Any
def getCheckmates(board):
    for l in board.legal_moves:
        localBoard = chess.Board(board.board_fen())
        localBoard.push(l)
        if(localBoard.is_checkmate()):
            return l
    return None

# Checks for Checkmates if any or else returns a random Move 
def getRandomMove(board):

    if(not getCheckmates(board)==None):
        return getCheckmates(board)
    else:
        rNo = random.randrange(0,board.legal_moves.count())
        i = 0
        for l in board.legal_moves:
            global a
            if(i==rNo):
                a = str(l)
                break
            i = i+1
        return a
    

def mostValuableCapture(board,move):
    pass