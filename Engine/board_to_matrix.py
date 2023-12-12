import chess
import numpy as np
import re


board = chess.Board(chess.Board.starting_fen)

print(board)



def moves_to_matrix(board:chess.Board):
    pieces = ['p','k','b','r','q','k']
    layers = []

    for piece in pieces:
        layers.append(create_rep_layer(board,piece))

    board_rep = np.stack(layers)

    return board_rep

def create_rep_layer(board:chess.Board,type:str):
    s = str(board)
    s = re.sub(f"[^{type}{type.upper()}  \n]",".",s)
    s = re.sub(f"{type}","-1",s)
    s = re.sub(f"{type.upper()}","1",s)
    s = re.sub(f"\.","0",s)

    board_mat = []

    for row in s.split('\n'):
        row = row.split(' ')
        row = [int(x) for x in row]
        board_mat.append(row)
        
    return np.array(board_mat)


print("      ")
print(moves_to_matrix(board))