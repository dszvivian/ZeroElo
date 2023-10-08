import chess
import random
from generateMove import getRandomMove,getBestMove,getStockFishmove
from renderBoard import renderBoard


def getMovefromUser():
    userMove = input("Enter the move: (ie:e2e4)")
    user_move = chess.Move.from_uci(str(userMove))
    return user_move



def startHumanVsBot(board:chess.Board):
    renderBoard(board)
    while not board.is_game_over():
        user_move = getMovefromUser()
        if(user_move in board.legal_moves):
            board.push(user_move)

            if(not board.is_game_over()):
                board.push(getBestMove(board))
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
                board.push(getBestMove(board))
                moves += 1
                renderBoard(board)
            else:
                renderBoard(board)
        else:
            print("Illegal Move")

    print(moves)



def startHumanVsStockfishBot(board:chess.Board):
    renderBoard(board)
    while not board.is_game_over():
        user_move = getMovefromUser()
        if(user_move in board.legal_moves):
            board.push(user_move)

            if(not board.is_game_over()):
                move = chess.Move.from_uci(str(getStockFishmove(board)))
                board.push(move)
                renderBoard(board)
            else:
                renderBoard(board)
        else:
            print("Illegal Move")

    
    
    




