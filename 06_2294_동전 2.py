import sys
# 2294 문제 - 동전
from collections import deque

sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
queue = deque()
nums_arr = list()
visit_arr = set()

for _ in range(n):
    tmp_num = int(input())
    queue.append((tmp_num, tmp_num, 1))
    nums_arr.append(tmp_num)
    visit_arr.add(tmp_num)


def BFS(que, key):
    while que:
        std_vertex = queue.popleft()
        std_sum = std_vertex[1]
        std_counter = std_vertex[2]

        if std_sum == key:
            print(std_counter)
            return

        for num in nums_arr:
            next_value = num
            next_sum = std_sum + num
            next_counter = std_counter + 1

            if next_sum <= key and next_sum not in visit_arr:
                next_vertex = (next_value, next_sum, next_counter)
                queue.append(next_vertex)
                visit_arr.add(next_sum)

    print(-1)


BFS(queue, k)