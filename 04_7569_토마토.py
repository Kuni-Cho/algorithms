import sys
# 2178 문제 - 미로 탐색
from collections import deque

sys.stdin = open("input.txt", "r")

M, N, H = map(int, input().split())

tomato_boxes = list()

for i in range(H):
    tmp_list = list()
    for j in range(N):
        tmp_list.append(list(map(int, input().split())))
    tomato_boxes.append(tmp_list)


def checkMatrix(h, n, m, arr, que, visit_arr):
    flag = True
    for i in range(h):
        for j in range(n):
            if 0 in arr[i][j]:
                flag = False
            for k in range(m):
                if arr[i][j][k] == 1:
                    que.append((i, j, k, 0))
                    visit_arr[i][j][k] = 1
    return flag


def checkMatrix2(h, n, arr):
    for i in range(h):
        for j in range(n):
            if 0 in arr[i][j]:
                return True


def BFS(m, n, h, arr):
    queue = deque()
    final_count = 0
    rows_arr = [-1, 1, 0, 0, 0, 0]
    columns_arr = [0, 0, -1, 1, 0, 0]
    levels_arr = [0, 0, 0, 0, -1, 1]
    visit_arr = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
    if checkMatrix(h, n, m, arr, queue, visit_arr):
        print(0)
        return

    while queue:
        std_vertex = queue.popleft()
        final_count = std_vertex[3]
        for i in range(6):
            next_level = std_vertex[0] + levels_arr[i]
            next_row = std_vertex[1] + rows_arr[i]
            next_column = std_vertex[2] + columns_arr[i]
            next_count = std_vertex[3] + 1
            if 0 <= next_level < h and 0 <= next_row < n and 0 <= next_column < m and arr[next_level][next_row][
                next_column] == 0 and visit_arr[next_level][next_row][next_column] == 0:
                arr[next_level][next_row][next_column] = 1
                visit_arr[next_level][next_row][next_column] = 1
                next_vertex = (next_level, next_row, next_column, next_count)
                queue.append(next_vertex)

    if checkMatrix2(h, n, arr):
        print(-1)
    else:
        print(final_count)


BFS(M, N, H, tomato_boxes)
