import chess
import random
from generateMove import getRandomMove
from renderBoard import renderBoard

board = chess.Board(chess.Board.starting_fen) #Load the starting position
print(board)





def startHumanVsBot(board):
    while not board.is_game_over():
        userMove = input("Enter the move: (ie:e2e4)")
        user_move = chess.Move.from_uci(str(userMove))
        if(user_move in board.legal_moves):
            board.push(user_move)

            if(not board.is_game_over()):
                engine_move = chess.Move.from_uci(getRandomMove(board))
                board.push(engine_move)
                renderBoard(board)
            else:
                renderBoard(board)
        else:
            print("Illegal Move")





    
    
    




