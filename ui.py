import chess
import chess.svg

board = chess.Board("3r4/8/R7/2P1krp1/3p4/1B3R2/P7/2K2n2 w - - 4 57") #Load the starting position
print(board)

# Returns a first move on each type
def getFirstMove(board):
    for l in board.legal_moves:
        global a
        a = str(l)
        break
    return a 


while not board.is_game_over():
    userMove = input("Enter the move: (ie:e2e4)")
    user_move = chess.Move.from_uci(str(userMove))
    if(user_move in board.legal_moves):
        board.push(user_move)

        if(not board.is_game_over()):
            engine_move = chess.Move.from_uci(getFirstMove(board))
            board.push(engine_move)
            print(board)
        else:
            print(board)
    else:
        print("Illegal Move")
    
    
    




