import copy
import sys

# 1987 문제 - 알파벳

sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(100000)

row, column = map(int, sys.stdin.readline().rstrip().split())
matrix = list()
for _ in range(row):
    matrix.append(list(map(lambda x: ord(x) - 65, sys.stdin.readline().rstrip())))

visit_arr = [0] * 26
visit_arr[matrix[0][0]] = 1
row_arr, column_arr = [-1, 1, 0, 0], [0, 0, -1, 1]
step = 1
result = 0


def DFS(s_r, s_c):
    global step, result
    result = max(result, step)
    for i in range(4):
        n_r = s_r + row_arr[i]
        n_c = s_c + column_arr[i]
        if 0 <= n_r < row and 0 <= n_c < column and visit_arr[matrix[n_r][n_c]] == 0:
            visit_arr[matrix[n_r][n_c]] = 1
            step += 1
            DFS(n_r, n_c)
            visit_arr[matrix[n_r][n_c]] = 0
            step -= 1


DFS(0, 0)

print(result)
