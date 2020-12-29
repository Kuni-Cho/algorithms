import sys

# 2573 문제 - 빙산

# stack으로 풀어보자

sys.stdin = open("input.txt", "r")
row, column = map(int, input().split())
visit_arr = [[0] * column for _ in range(row)]
matrix = list()
matrix_copy = list()

rows_arr, columns_arr = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(row):
    tmp_input = input()
    matrix.append(list(map(int, tmp_input.split())))
    matrix_copy.append(list(map(int, tmp_input.split())))


def DFS(s):
    while s:
        tmp_location = s.pop()
        tmp_r = tmp_location[0]
        tmp_c = tmp_location[1]
        tmp_count = 0
        for i in range(4):
            nr = tmp_r + rows_arr[i]
            nc = tmp_c + columns_arr[i]

            if 0 <= nr < row and 0 <= nc < column and matrix[nr][nc] == 0:
                tmp_count += 1
            elif 0 <= nr < row and 0 <= nc < column and visit_arr[nr][nc] == 0:
                s.append((nr, nc))
                visit_arr[nr][nc] = 1
        if tmp_count > 0:
            matrix_copy[tmp_r][tmp_c] = matrix_copy[tmp_r][tmp_c] - tmp_count
            if matrix_copy[tmp_r][tmp_c] < 0:
                matrix_copy[tmp_r][tmp_c] = 0


year = 0
while True:
    stack = list()
    count = 0
    sum_nums = 0
    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                continue
            elif matrix[i][j] != 0 and visit_arr[i][j] == 0:
                stack.append((i, j))
                visit_arr[i][j] = 1
                DFS(stack)
                count += 1
                sum_nums = sum_nums + matrix[i][j]
    if count > 1:
        print(year)
        break
    elif sum_nums == 0:
        print(0)
        break
    else:
        for i in range(row):
            for j in range(column):
                visit_arr[i][j] = 0
                matrix[i][j] = matrix_copy[i][j]
        year += 1


