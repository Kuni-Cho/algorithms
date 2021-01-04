import sys

sys.stdin = open("input.txt", "r")

meetings = int(input())
meetings_arr = list()
counter = 1

for _ in range(meetings):
    meetings_arr.append(tuple(map(int, input().split())))

arranged_finish = sorted(meetings_arr, key=lambda x: (x[1], x[0]))

std_meeting = arranged_finish[0]

for schedule in arranged_finish[1:]:
    if schedule[0] >= std_meeting[1]:
        counter += 1
        std_meeting = schedule

print(counter)

