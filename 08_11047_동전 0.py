import bisect
import sys

sys.stdin = open("input.txt", "r")

N, K = map(int, sys.stdin.readline().rstrip().split())

coin_arr = list()
target = K
result = 0

for _ in range(N):
    coin_arr.append(int(sys.stdin.readline().rstrip()))

while target != 0:
    tmp_idx = bisect.bisect(coin_arr, target)
    tmp_coin = coin_arr[tmp_idx - 1]
    tmp_coin_amount = target // tmp_coin
    tmp_remains = target % tmp_coin
    result += tmp_coin_amount
    target = tmp_remains

print(result)



