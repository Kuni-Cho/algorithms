import sys
# 1260번 문제
from collections import deque

sys.stdin = open("input.txt", "r")

edge_arr = list()

N, M, V = map(int, input().split())
for _ in range(M):
    edge_arr.append(list(map(int, input().split())))

stack = deque()
queue = deque()


def BFS(v, arr):
    visit_list = []
    queue.append(v)

    while queue:
        std_vertex = queue.popleft()
        if std_vertex not in visit_list:
            print(std_vertex, end=" ")
            visit_list.append(std_vertex)
            tmp_vertex_arr = list()

            for edge in arr:
                linked_v1 = edge[0]
                linked_v2 = edge[1]
                if linked_v1 == std_vertex:
                    tmp_vertex_arr.append(linked_v2)
                elif linked_v2 == std_vertex:
                    tmp_vertex_arr.append(linked_v1)

            tmp_vertex_arr.sort()

            for tmp_v in tmp_vertex_arr:
                queue.append(tmp_v)


def DFS(v, arr):
    visit_list = []
    stack.append(v)

    while stack:
        std_vertex = stack.pop()
        if std_vertex not in visit_list:
            print(std_vertex, end=" ")
            visit_list.append(std_vertex)
            tmp_vertex_arr = list()

            for edge in arr:
                linked_v1 = edge[0]
                linked_v2 = edge[1]
                if linked_v1 == std_vertex:
                    tmp_vertex_arr.append(linked_v2)
                elif linked_v2 == std_vertex:
                    tmp_vertex_arr.append(linked_v1)

            tmp_vertex_arr.sort(reverse=True)

            for tmp_v in tmp_vertex_arr:
                stack.append(tmp_v)

DFS(V, edge_arr)
print("\n", end="")
BFS(V, edge_arr)

