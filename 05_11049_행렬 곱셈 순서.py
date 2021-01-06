import math
import sys

sys.stdin = open("input.txt", "r")

N = int(input())

matrix_list = list()

for _ in range(N):
    matrix_list.append(tuple(map(int, input().split())))


def multiple_m():
    dp_arr = [[0] * N for _ in range(N)]

    for i in range(1):
        for j in range(N):
            tmp_row = i
            tmp_column = j
            for k in range(N - j):
                if tmp_row == tmp_column:
                    dp_arr[tmp_row][tmp_column] = 0
                    tmp_row += 1
                    tmp_column += 1
                    continue
                else:
                    tmp = math.inf
                    for l in range(tmp_row, tmp_column):
                        dp_arr[tmp_row][tmp_column] = min(tmp,
                                                          dp_arr[tmp_row][l] + dp_arr[l + 1][tmp_column] + (
                                                                  matrix_list[tmp_row][0] * matrix_list[l][1] *
                                                                  matrix_list[tmp_column][1]))
                        tmp = dp_arr[tmp_row][tmp_column]
                    tmp_row += 1
                    tmp_column += 1

    for row in dp_arr:
        print(row)

    print(dp_arr[0][N - 1])


multiple_m()
