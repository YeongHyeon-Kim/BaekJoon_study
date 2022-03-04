import sys
from collections import Counter

input = sys.stdin.readline


N = int(input())

max_v = -4000
min_v = 4000

sum_v = 0
li = []
mode_max = [0]*8001

for i in range(N):
    num = int(input())

    if num > max_v:
        max_v = num
    if min_v > num:
        min_v = num

    sum_v += num  # 중앙값 체크
    li.append(num)

li.sort()


print(round(sum_v / N))
print(li[N//2])

mode = Counter(li)
mode = mode.most_common(2)


if len(mode) >= 2:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])

print(max_v - min_v)
