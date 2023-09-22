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

# Returns a first move on each type
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


while not board.is_game_over():

    if(not board.legal_moves.count==0):
        print(board.legal_moves)
        bot1_move = chess.Move.from_uci(getRandomMove(board))
        board.push(bot1_move)
        print(board)
        print(" ")

    else:
        print("CheckMate")
        print(board.legal_moves)

    