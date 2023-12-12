import chess
from evaluate import calculatePosition
from evaluateExp import move_value,evaluateBoard


MATE_SCORE = 1000000000

#for now it returns only capturing moves 
def getOrderedMoves(board:chess.Board)->list[chess.Move]:
    
    def orderer(move:chess.Move):
        return move_value(board,move)
    
    return sorted(board.legal_moves,key=orderer,reverse=(board.turn==chess.BLACK))



def minimax(board:chess.Board,depth:int)->chess.Move:
    """
    returns the best move.
    gets the best possible score using minimax search for a given depth
    """

    maximize = board.turn == chess.WHITE

    if(maximize):
        score = -float("inf")
    else:
        score = float("inf")

    moves = getOrderedMoves(board)
    # print(moves)
    best_move = None

    for l in moves:
        board.push(l)
        move_score = minimaxSearch(board,depth-1,color=not maximize)#Returns best possible move at that level
        # print(move_score)
        board.pop()

        if(maximize==True and move_score>=score):
            best_move = l
            score = move_score
        elif(maximize==False and move_score<=score):
            best_move = l
            score = move_score

    return best_move


def minimaxSearch(board:chess.Board,depth:int,color:bool)->float:
    if(depth==0):
        return evaluateBoard(board)
    
    if(board.is_checkmate):
        return MATE_SCORE if color==False else -MATE_SCORE
    
    #probably due to a draw or stalemate        
    if(board.is_game_over()):
        return 0
    
    maxEval = -float("inf")
    minEval = float("inf")

    for l in board.legal_moves:
        board.push(l)

        eval = minimaxSearch(board,depth-1,not color)
        
        if(color==True and eval>=maxEval):
            maxEval = eval
            board.pop()
            return maxEval
        elif(color==False and eval<=minEval):
            minEval = eval
            board.pop()
            return minEval
        
    if(color):
        return maxEval
    else:
        return minEval
    
board = chess.Board(chess.Board.starting_fen)
print(getOrderedMoves(board))
