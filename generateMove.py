import chess
import random
from evaluate import retBestCaptureMove
from search import minimax
from stockfish import Stockfish


# Returns CheckMates if Any
def getCheckmates(board:chess.Board):
    for l in board.legal_moves:
        localBoard = chess.Board(board.board_fen())
        localBoard.push(l)
        if(localBoard.is_checkmate()):
            return l
    return None

def getFirstMove(board):
    for l in board.legal_moves:
        global a
        a = str(l)
        break
    return a 

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
            # print(l)
            capturing_moves.append(l)

    if(len(capturing_moves)<=0):
        return None
    else:
        #Get the Best capture
        return retBestCaptureMove(board,capturing_moves)
    
def getBestCaptureRec(board:chess.Board):
    return minimax(board,3)
          

def getBestMove(board:chess.Board):
    if(getCheckmates(board)!=None):#Check for Checkmates
        return getCheckmates(board)
    if(getBestCaptureRec(board)!=None):
        return getBestCaptureRec(board)
    else:
        return getRandomMove(board)
    
def getStockFishmove(board:chess.Board):
    stockfish = Stockfish("stockfish.exe")
    stockfish.set_fen_position(board.board_fen)
    move = stockfish.get_best_move()
    print(move)
    return move

    


board = chess.Board(chess.Board.starting_fen)

print(getStockFishmove(board))