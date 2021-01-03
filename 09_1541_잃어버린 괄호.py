import sys

sys.stdin = open("input.txt", "r")

case = sys.stdin.readline().rstrip()

test = case.split("-")
result_arr = list()

for num in test:
    tmp_arr = num.split("+")
    tmp_result = 0
    for tmp_num in tmp_arr:
        tmp_result += int(tmp_num)
    result_arr.append(tmp_result)

result = result_arr[0]

for num2 in result_arr[1:]:
    result -= num2

print(result)