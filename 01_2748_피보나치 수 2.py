import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().rstrip())
dp_arr = [-1] * (n + 1)


def fibo(n):
    if n == 1 or n == 2:
        return 1
    elif dp_arr[n] > -1:
        return dp_arr[n]
    elif n > 2:
        dp_arr[n] = fibo(n - 2) + fibo(n - 1)
        return dp_arr[n]


print(fibo(n))
