import chess
from GameLoop import startHumanVsBot



board = chess.Board(chess.Board.starting_fen) #Load the starting position

startHumanVsBot(board)