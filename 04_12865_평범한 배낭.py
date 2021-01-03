import sys

sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
input_list = list()
dp_arr = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    input_list.append(tuple(map(int, input().split())))


def knapsack():
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            item = input_list[i - 1]
            item_weight = item[0]
            item_value = item[1]


            if item_weight > j:
                dp_arr[i][j] = dp_arr[i - 1][j]

            else:
                remain_value = dp_arr[i - 1][j - item_weight]
                dp_arr[i][j] = max((item_value + remain_value), dp_arr[i - 1][j])


knapsack()

print(dp_arr[N][K])

