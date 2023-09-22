import chess
import chess.svg
import random

board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR") 



def getRandomMove(board):

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