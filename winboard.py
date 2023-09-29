import chess
from GameLoop import startHumanVsBot
from generateMove import getBestMove

board = chess.Board(chess.Board.starting_fen) #Load the starting position

def command(board:chess.Board,msg:str):
    user_move = chess.Move.from_uci(msg)
    if(user_move in board.legal_moves):
        board.push(user_move)
        if(not board.is_game_over()):
            board.push(getBestMove(board))
        else:
            return
    else:
        return
    

def startWinboard(board:chess.Board):
    while True:
        msg = input()
        command(board,msg)

startWinboard(board)