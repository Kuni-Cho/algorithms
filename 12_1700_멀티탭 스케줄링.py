import sys

sys.stdin = open("input.txt", "r")

holes, usages = map(int, input().split())

usages_arr = list(map(int, input().split(" ")))
items_arr = [[] for _ in range(usages + 1)]


class Socket:
    def __init__(self, capa):
        self.capacity = capa
        self.holes = list()

    def isFUll(self):
        if len(self.holes) == self.capacity:
            return True
        else:
            return False


for idx, usage in enumerate(usages_arr):
    items_arr[usage].append(idx + 1)

multi_tap = Socket(holes)
result = 0

for usage in usages_arr:
    if multi_tap.isFUll():
        if usage in multi_tap.holes:
            del items_arr[usage][0]
        else:
            tmp = 0
            tmp_item = 0
            for item_plug in multi_tap.holes:
                if len(items_arr[item_plug]) > 0 and tmp < items_arr[item_plug][0]:
                    tmp = items_arr[item_plug][0]
                    tmp_item = item_plug
                elif len(items_arr[item_plug]) == 0:
                    tmp_item = item_plug
                    break
            multi_tap.holes.remove(tmp_item)
            result += 1
            multi_tap.holes.append(usage)
            del items_arr[usage][0]
    else:
        if usage in multi_tap.holes:
            del items_arr[usage][0]
        else:
            multi_tap.holes.append(usage)
            del items_arr[usage][0]

print(result)
