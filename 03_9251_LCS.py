import sys

sys.stdin = open("input.txt", "r")

first_str = "0" + sys.stdin.readline().rstrip()
second_str = "0" + sys.stdin.readline().rstrip()
"0ACP"
"0CAPCA"
len_f = len(first_str)
len_s = len(second_str)

dp_matrix = [[0 for _ in range(len_f)] for _ in range(len_s)]

for i in range(1, len_f):
    for j in range(1, len_s):

        if first_str[i] == second_str[j]:
            dp_matrix[j][i] = dp_matrix[j - 1][i - 1] + 1

        else:
            dp_matrix[j][i] = max(dp_matrix[j - 1][i], dp_matrix[j][i - 1])

print(dp_matrix[len_s - 1][len_f - 1])
#
# i = len_f - 1
# j = len_s - 1
# result_arr = list()
#
# while i > 0 and j > 0:
#     if first_str[i] == second_str[j]:
#         print(i, j)
#         result_arr.append(first_str[i])
#         i -= 1
#         j -= 1
#     else:
#         if dp_matrix[i][j - 1] > dp_matrix[i - 1][j]:
#             j -= 1
#         else:
#             i -= 1
#
# for i in range(len(result_arr)):
#     print(result_arr.pop(), end="")
