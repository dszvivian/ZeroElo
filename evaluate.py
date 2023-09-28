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
            blackPiece = piece.piece_type
            score += piece_value.get(blackPiece)

    return score

def retBestCaptureMove(board:chess.Board,captures:list[chess.Move])->chess.Move:
    score = 0
    best_move = None
    for l in captures:
        if(captureScore(board,l)>=score):
            score = captureScore(board,l)
            best_move = l
    return best_move

#Calculates & returns the diff b/w currentBoardScore and scoreAfterTheMove
#Returns only if it is >= 0
def captureScore(board:chess.Board,move:chess.Move)->int:
    local_board = board
    firstPosScore = calculatePosition(local_board,False)
    print(firstPosScore)
    local_board.push(move)
    nextPosScore = calculatePosition(local_board,False)
    print(nextPosScore)
    score = nextPosScore - firstPosScore

    if(score>=0):
        return score
    else:
        return -1
    

# board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
# print(renderBoard(board))
# print(board.legal_moves)

# move = chess.Move.from_uci('e2e4')
# print(captureScore(board,move))
# board.push(move)
# print(renderBoard(board))

