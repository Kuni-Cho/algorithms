import math
import sys

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
stones_arr = [0] * (N + 1)
max_d = int(math.sqrt(2 * N)) + 1

for _ in range(M):
    stones_arr[int(input())] = 1

dp_arr = [[math.inf] * (max_d + 1) for _ in range(N + 1)]

dp_arr[1][0] = 0

for i in range(2, N + 1):
    if stones_arr[i] == 1:
        continue

    for j in range(1, max_d):
        dp_arr[i][j] = min(dp_arr[i - j][j + 1], dp_arr[i - j][j], dp_arr[i - j][j - 1]) + 1

result = min(dp_arr[N])

if result == math.inf:
    print(-1)
else:
    print(result)
