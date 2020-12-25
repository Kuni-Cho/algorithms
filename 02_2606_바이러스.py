import sys
# 1260번 문제
from collections import deque

sys.stdin = open("input.txt", "r")

nums_computer = int(input())
syncs_case = int(input())
visit_arr, syncs_arr = list(), list()
queue = deque()

for _ in range(nums_computer):
    tmp_arr = list()
    syncs_arr.append(tmp_arr)

for _ in range(syncs_case):
    start_v, end_v = map(int, input().split())
    syncs_arr[start_v - 1].append(end_v)
    syncs_arr[end_v - 1].append(start_v)


def BFS(start, syncs_array, visit_array):
    queue.append(start)
    cnt = 0

    while queue:
        std_vertex = queue.popleft()
        visit_arr.append(std_vertex)
        cnt += 1
        for v in syncs_array[std_vertex - 1]:
            if v not in visit_array:
                queue.append(v)
                visit_arr.append(v)
    return cnt - 1


print(BFS(1, syncs_arr, visit_arr))

