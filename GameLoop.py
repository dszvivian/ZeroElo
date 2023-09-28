import chess
import random
from generateMove import getRandomMove,getBestMove
from renderBoard import renderBoard


def getMovefromUser():
    userMove = input("Enter the move: (ie:e2e4)")
    user_move = chess.Move.from_uci(str(userMove))
    return user_move



def startHumanVsBot(board):
    while not board.is_game_over():
        user_move = getMovefromUser()
        if(user_move in board.legal_moves):
            board.push(user_move)

            if(not board.is_game_over()):
                board.push(getBestMove(board))
                print(board)
                # renderBoard(board)
            else:
                print(board)
                # renderBoard(board)
        else:
            print("Illegal Move")


def startBotVsBot(board):
    pass



    
    
    




