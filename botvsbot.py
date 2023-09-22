import chess
import random

board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR") #Load the starting position


# Returns a first move on each type
def getFirstMove(board):
    for l in board.legal_moves:
        global a
        a = str(l)
        break
    return a 

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


moves = 0
while not board.is_game_over():

    if(not board.legal_moves.count==0):
        user_move = chess.Move.from_uci(getRandomMove(board))
        board.push(user_move)
        moves += 1
        
print(moves)
print(board)

    