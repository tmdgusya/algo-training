from utils import print2DimArr
from copy import deepcopy

"""
chess board will be n*n

0,0 each row has same x-axis index, and each row has same y-axis index will be protected to not be able to put chess
"""

answer = []

"""
this function helps to draw protected areas on tha board
"""
def draw(x, y, board):
    drawed = []
    for i in range(len(board)):
        for j in range(len(board)):
            if i == x or j == y or abs(i - x) == abs(j - y):
                if board[i][j] == 1:
                    board[i][j] = 0
                    drawed.append((i, j))
    return drawed
    
def undraw(board, drawed):
    for x,y in drawed:
        board[x][y] = 1

def chess(acc, board, depth):
    if len(acc) == len(board):
        answer.append(deepcopy(acc))
        return

    for i in range(len(board)):
        if board[depth][i] == 0:
            continue
        # draw
        drawed = draw(depth, i, board)
        acc.append([depth, i])
        chess(acc, board, depth + 1)
        # cancel draw
        acc.pop()
        undraw(board, drawed)

    return

input = 8
board = [[1 for _ in range(input)] for _ in range(input)]
acc = []
chess(acc, board, 0)
print(f'numbers of possible combinations: {len(answer)}')