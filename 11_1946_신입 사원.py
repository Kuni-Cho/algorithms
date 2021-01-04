import sys

sys.stdin = open("input.txt", "r")

case = int(sys.stdin.readline().rstrip())

for _ in range(case):
    each_case = int(sys.stdin.readline().rstrip())

    first_score_arr = [0] * (each_case + 1)
    second_score_arr = [0] * (each_case + 1)

    result = 0
    min_value = each_case + 1

    for _ in range(each_case):
        f, s = map(int, input().split())

        first_score_arr[f] = s

    for idx, num in enumerate(first_score_arr[1:]):
        min_value = min(min_value, num)
        second_score_arr[idx + 1] = min_value

    for i in range(1, each_case + 1):
        if first_score_arr[i] <= second_score_arr[i]:
            result += 1

    print(result)
