import numpy as np


def possibleNumberInference(board):
    possible = np.ones((9, 9, 9), dtype=bool)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = board[i][j]
                possible[i][j] = False
                for k in range(9):
                    possible[i][k][num - 1] = False
                    possible[k][j][num - 1] = False
                box_i = (i // 3) * 3
                box_j = (j // 3) * 3 
                for k in range(3):
                    for l in range(3):
                        possible[box_i + k][box_j + l][num - 1] = False
    return possible


def lastRemainingCellInference(board):
    possible = possibleNumberInference(board)
    # 逐行遍历

    # 打印possible [i, j]:possible[i][j]
    # print("-" * 50)
    # for i in range(9):
    #     for j in range(9):
    #         possible_numbers = [num + 1 for num in range(9) if possible[i][j][num]]
    #         print(f"{i}, {j}: {possible_numbers}")
    # print("-" * 50)
    flag = False

    for i in range(9):
        for num in range(9):
            cnt = 0
            pos = -1
            for j in range(9):
                if possible[i][j][num]:
                    cnt += 1
                    pos = j
            if cnt == 1:
                board[i][pos] = num + 1
                # possible = possibleNumberInference(board)
                # return True
                flag = True
    # 逐列遍历
    for j in range(9):
        for num in range(9):
            cnt = 0
            pos = -1
            for i in range(9):
                if possible[i][j][num]:
                    cnt += 1
                    pos = i
            if cnt == 1:
                board[pos][j] = num + 1
                # possible = possibleNumberInference(board)
                # return True
                flag = True
    # 逐3x3小格遍历
    for i in range(3):
        for j in range(3):
            for num in range(9):
                cnt = 0
                pos = (-1, -1)
                for k in range(3):
                    for l in range(3):
                        if possible[i * 3 + k][j * 3 + l][num]:
                            cnt += 1
                            pos = (i * 3 + k, j * 3 + l)
                if cnt == 1:
                    board[pos[0]][pos[1]] = num + 1
                    # possible = possibleNumberInference(board)
                    # return True
                    flag = True
    if flag:
        # print("board changed")
        return True
    return False


board = np.array(
    [
        [2, 0, 0, 0, 7, 0, 0, 3, 8],
        [0, 0, 0, 0, 0, 6, 0, 7, 0],
        [3, 0, 0, 0, 4, 0, 6, 0, 0],
        [0, 0, 8, 0, 2, 0, 7, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 7, 0, 3, 0, 4, 0, 0],
        [0, 0, 4, 0, 8, 0, 0, 0, 9],
        [0, 6, 0, 4, 0, 0, 0, 0, 0],
        [9, 1, 0, 0, 6, 0, 0, 0, 2],
    ]
)

while True:
    if not lastRemainingCellInference(board):
        break
# print("No more cells can be filled.")

print("Final board:")
print(board)
