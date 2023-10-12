import chess
from GameLoop import startHumanVsBot,startBotVsBot,startHumanVsStockfishBot

board = chess.Board(chess.Board.starting_fen) #Load the starting position

startHumanVsBot(board)
# startBotVsBot(board)

# startHumanVsStockfishBot(board)