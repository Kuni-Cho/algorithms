import sys
from collections import deque

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
adj_list_reverse = [[] for _ in range(N + 1)]
visit_arr = [0 for _ in range(N + 1)]
queue = deque()

for i in range(M):
    f_student, b_student = map(int, input().split())
    adj_list[f_student].append(b_student)
    adj_list_reverse[b_student].append(f_student)

while sum(visit_arr) != N:
    for i in range(1, N + 1):
        if not adj_list_reverse[i] and visit_arr[i] == 0:
            print(i)
            visit_arr[i] = 1
            for num in adj_list[i]:
                adj_list_reverse[num].remove(i)
