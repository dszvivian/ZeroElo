import chess
import numpy as np



row_to_letter = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}

column_to_number = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}


board = chess.Board(chess.Board.starting_fen)

move = chess.Move.from_uci("e2e4")

# move in uciu format
def move_to_matrix(move):
    move = str(move)

    from_matrix = np.zeros((8,8))
    from_row_index = 8 -int(move[1])
    from_column_index = column_to_number[move[0]]-1
    from_matrix[from_row_index][from_column_index] = 1

    to_matrix = np.zeros((8,8))
    to_row_index = 8 -int(move[3])
    to_column_index = column_to_number[move[2]]-1
    to_matrix[to_row_index][to_column_index] = 1

    return np.stack([from_matrix,to_matrix])



def create_move_list(movesList):
    return movesList.split(' ')


print(create_move_list('d4 d5 c4 c6 cxd5 e6 dxe6 fxe6 Nf3 Bb4+ Nc3 Ba5 Bf4'))