import sys
# 2178 문제 - 미로 탐색
from collections import deque

sys.stdin = open("input.txt", "r")

N, M = map(int, sys.stdin.readline().split())
matrix = list()

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().strip())))


def BFS(start_row, start_column, m, n, arr):
    queue = deque()
    rows = [-1, 1, 0, 0]
    columns = [0, 0, -1, 1]
    visit_matrix = [[0 for x in range(M)] for y in range(N)]
    visit_matrix[start_row][start_column] = 1
    queue.append((start_row, start_column, 1))

    while queue:
        tmp_vertex = queue.popleft()
        tmp_row = tmp_vertex[0]
        tmp_column = tmp_vertex[1]
        tmp_count = tmp_vertex[2]

        for i in range(4):
            next_row = tmp_row + rows[i]
            next_column = tmp_column + columns[i]
            if 0 <= next_row < n and 0 <= next_column < m and arr[next_row][next_column] == 1 and \
                    visit_matrix[next_row][next_column] == 0:

                next_vertex_data = (next_row, next_column, tmp_count + 1)
                queue.append(next_vertex_data)
                visit_matrix[next_row][next_column] = 1

                if next_row == (n - 1) and next_column == (m - 1):
                    return next_vertex_data[2]


print(BFS(0, 0, M, N, matrix))
