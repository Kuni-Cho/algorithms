import sys
from collections import deque

sys.stdin = open("input.txt", "r")

N = int(input())
M = int(input())

parts_array = [0 for _ in range(N + 1)]
adj_list = [[] for _ in range(N + 1)]
inDegree_arr = [0] * (N + 1)

for _ in range(M):
    X, Y, K = map(int, input().split())
    adj_list[X].append((Y, K))
    inDegree_arr[Y] += 1

queue = deque()
queue.append(N)
parts_array[N] = 1

while queue:
    curr_node = queue.popleft()

    for node in adj_list[curr_node]:
        inDegree_arr[node[0]] -= 1
        parts_array[node[0]] += node[1] * parts_array[curr_node]

        if inDegree_arr[node[0]] == 0:
            queue.append(node[0])

for idx, num in enumerate(parts_array):
    if not adj_list[idx] and idx > 0:
        print(idx, num)
