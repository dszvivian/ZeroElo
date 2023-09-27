import chess

piece_value = {
    chess.PAWN: 100,
    chess.KNIGHT: 400,
    chess.BISHOP: 400,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 2000
}


#for now since the bot is black by default 
def calculateBlackPosition(board:chess.Board)->int:
    score = 0
    for sqaure in chess.Square:
        piece = board.piece_at(sqaure)
        if(piece.color==chess.BLACK):
            value = piece.piece_type
        #incomplete


def isGoodCapture(board:chess.Board,move:chess.Move):
    pass