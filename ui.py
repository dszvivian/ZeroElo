import chess
import chess.svg

board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR") #Load the starting position

# Returns a first move on each type
def getFirstMove(board):
    for l in board.legal_moves:
        global a
        a = str(l)
        break
    return a

 
while(True):
    userMove = input()
    user_move = chess.Move.from_uci(str(userMove))
    board.push(user_move)
    engine_move = chess.Move.from_uci(getFirstMove(board))
    board.push(engine_move)
    print(board)

    




