import chess
import chess.svg

board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR") #Load the starting position


# basic pass N play chess 
while(True):
    userMove = input()
    move = chess.Move.from_uci(str(userMove))
    board.push(move)

    print(board)
    



