import chess
from renderBoard import renderBoard

piece_value = {
    chess.PAWN: 100,
    chess.KNIGHT: 400,
    chess.BISHOP: 400,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 2000
}

def calculatePosition(board:chess.Board):
    score = 0
    for sqaure in chess.SQUARES:
        piece = board.piece_at(sqaure)
        
        if(piece!=None):
            currentPiece = piece.piece_type
            if(piece.color==False):
                score -= piece_value.get(currentPiece)
            if(piece.color==True):
                score += piece_value.get(currentPiece)
    return score


#Whole point is to calculate how bad is the opponents  position after a capture
def captureScore(board:chess.Board,move:chess.Move)->int:
    local_board = chess.Board(board.board_fen())
    firstPosScore = calculatePosition(local_board)
    local_board.push(move)
    nextPosScore = calculatePosition(local_board)
    score = nextPosScore - firstPosScore
    return score

def retBestCaptureMove(board:chess.Board,captures:list[chess.Move])->chess.Move:
    score = 0
    best_move = None
    color = board.piece_at(captures[0].from_square).color #Return the opponents color
    for l in captures:
        capScore = captureScore(board,l)
        if(color==True):
            if(capScore>=score):
                score=capScore
                best_move = l
        else:
            if(capScore<=score):
                score = capScore
                best_move = l
    return best_move


# board = chess.Board("r1b1r1k1/p3qppp/2p5/3p4/nB6/2PB1Q2/P1PK1PPP/R6R w - - 9 16")
# m1 = chess.Move.from_uci("b4e7")
# print(captureScore(board,m1))







