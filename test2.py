import chess
import chess.svg
import random

board = chess.Board("5r1k/1p3R2/2p3Q1/p2p1p2/P2P3P/2P2B2/1P3P1K/2q5 w - - 2 43") 




def getCheckmates(board):
    for l in board.legal_moves:
        localBoard = chess.Board(board.board_fen())
        localBoard.push(l)
        if(localBoard.is_checkmate()):
            return l
    return None

def getRandomMove(board):

    if(not getCheckmates(board)==None):
        return getCheckmates(board)
    else:
        rNo = random.randrange(0,board.legal_moves.count())
        print(rNo)
        i = 0
        for l in board.legal_moves:
            global a
            if(i==rNo):
                a = str(l)
                break
            i = i+1
        return a 

print(board.legal_moves)
print(getRandomMove(board))