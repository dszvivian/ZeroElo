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


#for now False since the bot is black by default 
def calculatePosition(board:chess.Board,color:bool)->int:
    score = 0
    for sqaure in chess.SQUARES:
        piece = board.piece_at(sqaure)
        
        if(piece!=None and piece.color==color):
            currentPiece = piece.piece_type
            score += piece_value.get(currentPiece)

    return score


#Whole point is to calculate how bad is the opponents  position after a capture
def captureScore(board:chess.Board,move:chess.Move)->int:
    local_board = chess.Board(board.board_fen())
    firstPosScore = calculatePosition(local_board,True)
    local_board.push(move)
    nextPosScore = calculatePosition(local_board,True)
    score = nextPosScore - firstPosScore
    # print(firstPosScore,nextPosScore)
    return score

def retBestCaptureMove(board:chess.Board,captures:list[chess.Move])->chess.Move:
    score = 0
    best_move = None
    for l in captures:
        if(captureScore(board,l)<=score):
            score = captureScore(board,l)
            best_move = l
        else:
            return None
    
    return best_move


# board = chess.Board("rrb3k1/2q2Q1p/5p2/p2p1p2/P1pP1b2/2P4P/3N2PN/2R1R1K1 b - - 1 2")
# for l in board.legal_moves:
#     print(l)
# move = chess.Move.from_uci("c7f7")
# print(captureScore(board,move))





