import sys

sys.stdin = open("input.txt", "r")

case = int(input())


def tile2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        front_num = 1
        back_num = 2

        for i in range(n - 2):
            sum_num = (front_num + back_num) % 15746
            front_num = back_num
            back_num = sum_num

        return sum_num


print(tile2(case))
