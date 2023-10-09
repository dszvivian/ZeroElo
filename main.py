import chess
from GameLoop import startHumanVsBot,startBotVsBot,startHumanVsStockfishBot

board = chess.Board("rnbqk2r/1pp1bp2/p4p1p/3p4/8/2N2Q2/PPP2PPP/R1B1KB1R b KQkq - 1 11") #Load the starting position

# startHumanVsBot(board)
startBotVsBot(board)

# startHumanVsStockfishBot(board)