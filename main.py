import chess
from GameLoop import startHumanVsBot

board = chess.Board("r4rk1/pb3pp1/1p2pB1p/2bq4/6N1/3B4/PPP2PPP/R2Q1RK1 b - - 0 2") #Load the starting position

startHumanVsBot(board)