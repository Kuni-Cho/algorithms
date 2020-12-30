import sys

sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
median_num = (N + 1) // 2

adj_list = [[] for _ in range(N + 1)]
adj_list_max = [[] for _ in range(N + 1)]
result = 0

for _ in range(M):
    f_marble, b_marble = map(int, input().split())
    adj_list[f_marble].append(b_marble)
    adj_list_max[b_marble].append(f_marble)


def DFS(s_node, value_arr):
    global result
    stack = list()
    stack.append(s_node)
    visit_arr = [0] * (N + 1)
    visit_arr[s_node] = 1
    count = 0

    while stack:
        curr_node = stack.pop()

        if count >= median_num:
            result += 1
            break

        tmp_list = value_arr[curr_node]

        for num in tmp_list:
            if visit_arr[num] == 0:
                visit_arr[num] = 1
                stack.append(num)
                count += 1


for i in range(1, N + 1):
    DFS(i, adj_list)
    DFS(i, adj_list_max)

print(result)


# version 2
# N, M = map(int, input().split())
# median_num = (N + 1) // 2
#
# adj_list = [[] for _ in range(N + 1)]
# adj_list_max = [[] for _ in range(N + 1)]
# result = 0
#
# for _ in range(M):
#     f_marble, b_marble = map(int, input().split())
#     adj_list[f_marble].append(b_marble)
#     adj_list_max[b_marble].append(f_marble)
#
#
# def DFS(s_node, value_arr):
#     global result
#     stack = list()
#     stack.append(s_node)
#     count = 0
#     visit_arr = [0] * (N + 1)
#     visit_arr[s_node] = 1
#
#     while stack:
#         curr_node = stack.pop()
#
#         for num in value_arr[curr_node]:
#             if visit_arr[num] == 0:
#                 count += 1
#                 if count >= median_num:
#                     return 1
#                 stack.append(num)
#                 visit_arr[num] = 1
#
#     return 0
#
#
# for i in range(1, N + 1):
#     result += DFS(i, adj_list)
#     result += DFS(i, adj_list_max)
#
# print(result)