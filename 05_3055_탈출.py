import sys
# 3055 문제 - 탈출
from collections import deque

sys.stdin = open("input.txt", "r")

row, column = map(int, input().split())

matrix = list()
for _ in range(row):
    matrix.append(list(map(str, input())))


def checkMatrix(r, c, m_arr, v_arr, que):
    for i in range(r):
        for j in range(c):
            if m_arr[i][j] == "D":
                exit_location = (i, j)
            elif m_arr[i][j] == "S":
                hedgehog = (i, j, 0)
                v_arr[i][j] = 1
            elif m_arr[i][j] == "*":
                que.append((i, j, 0))
                v_arr[i][j] = 1
    que.append(hedgehog)

    return exit_location


def BFS(r, c, m_arr):
    queue = deque()
    visit_matrix = [[0 for _ in range(c)] for _ in range(r)]
    exit_location = checkMatrix(r, c, m_arr, visit_matrix, queue)
    rows_arr = [-1, 1, 0, 0]
    column_arr = [0, 0, -1, 1]

    while queue:
        std_vertex = queue.popleft()
        std_row = std_vertex[0]
        std_column = std_vertex[1]
        std_counter = std_vertex[2]
        std_value = m_arr[std_row][std_column]
        #
        # for rows in m_arr:
        #     print(rows)
        # print("------------------------------------------------" + str(std_counter))

        for i in range(4):
            next_row = std_row + rows_arr[i]
            next_column = std_column + column_arr[i]
            next_counter = std_counter + 1

            if std_value == "S":
                if 0 <= next_row < r and 0 <= next_column < c and visit_matrix[next_row][next_column] == 0 and \
                        visit_matrix[next_row][next_column] != "*" and m_arr[next_row][next_column] != "X":
                    next_vertex = (next_row, next_column, next_counter)
                    queue.append(next_vertex)
                    visit_matrix[next_row][next_column] = 1
                    m_arr[next_row][next_column] = "S"

                    if (next_row, next_column) == exit_location:
                        print(next_counter)
                        return
            elif std_value == "*":
                if 0 <= next_row < r and 0 <= next_column < c and visit_matrix[next_row][next_column] == 0 and \
                        m_arr[next_row][next_column] != "D" and m_arr[next_row][next_column] != "X":
                    next_vertex = (next_row, next_column, next_counter)
                    queue.append(next_vertex)
                    visit_matrix[next_row][next_column] = 2
                    m_arr[next_row][next_column] = "*"

    print("KAKTUS")


BFS(row, column, matrix)
