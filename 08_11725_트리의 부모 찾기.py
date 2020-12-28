import sys

# 11725 문제 - 트리의 부모 찾기

sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(100001)

case_num = int(input())

adjacency_list = [[] for _ in range(case_num + 1)]
parent_list = [None] * (case_num + 1)
visit_list = [0] * (case_num + 1)

for _ in range(case_num - 1):
    node1, node2 = map(int, input().split())
    adjacency_list[node1].append(node2)
    adjacency_list[node2].append(node1)


def DFS(s_node, p_list):
    visit_list[s_node] = 1
    for n_node in adjacency_list[s_node]:
        if visit_list[n_node] == 0:
            p_list[n_node] = s_node
            DFS(n_node, p_list)


DFS(1, parent_list)

for num in parent_list:
    if num is not None:
        print(num)
