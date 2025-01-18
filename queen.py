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
    right = y
    left = y
    drawed = []
    for i in range(x + 1, len(board)):
        board[i][y] = 0
        drawed.append([i,y])
        if (right + 1) < len(board) and board[i][right + 1] == 1:
            board[i][right + 1] = 0
            drawed.append([i,right + 1])
            right += 1
        if (left - 1) >= 0 and board[i][left - 1] == 1:
            board[i][left - 1] = 0
            drawed.append([i,left - 1])
            left -= 1
    return drawed

def undraw(board, drawed):
    for x,y in drawed:
        board[x][y] = 1


def chess(acc, board, depth):
    if len(acc) == len(board):
        answer.append(deepcopy(acc))
        return;

    for i in range(len(board)):
        if board[depth][i] == 0:
            continue;
        # draw
        drawed = draw(depth, i, board)
        acc.append([depth, i])
        chess(acc, board, depth + 1)
        # cancel draw
        acc.pop()
        undraw(board, drawed)

    return;

input = 5
board = [[1 for _ in range(input)] for _ in range(input)]
acc = []
chess(acc, board, 0)
print(answer)
print(f'numbers of possible comibnation: {len(answer)}')