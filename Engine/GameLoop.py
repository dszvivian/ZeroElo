import chess
import random
from generateMove import getRandomMove,getBestMove,getBestCaptureRec
from renderBoard import renderBoard


def getMovefromUser(board:chess.Board):
    userMove = input("Enter the move: (ie:e2e4)")
 
    try:
        user_move = chess.Move.from_uci(str(userMove))
        if user_move in board.legal_moves:
            return user_move
    except:
        getMovefromUser(board)
        
    

def startHumanVsBot(board:chess.Board):
    renderBoard(board)
    while not board.is_game_over():
        user_move = getMovefromUser(board)
        if(user_move in board.legal_moves):
            board.push(user_move)

            if(not board.is_game_over()):
                board.push(getBestCaptureRec(board))
                renderBoard(board)
            else:
                renderBoard(board)
        else:
            print("Illegal Move")


def startBotVsBot(board):
    renderBoard(board)
    moves = 0
    while not board.is_game_over():
        user_move = getBestMove(board)
        if(user_move in board.legal_moves):
            board.push(user_move)
            moves += 1
            renderBoard(board)
            if(not board.is_game_over()):
                board.push(getBestCaptureRec(board))
                moves += 1
                renderBoard(board)
            else:
                renderBoard(board)
        else:
            print("Illegal Move")

    print(moves)


