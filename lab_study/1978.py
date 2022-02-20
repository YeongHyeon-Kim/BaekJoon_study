import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().strip().split()))


checked = [False]*1001
checked[0] = True
checked[1] = True
for i in range(2, int(1000**0.5)+1):
    if not checked[i]:
        for j in range(i+i, 1001, i):
            checked[j] = True

co = 0
for i in nums:
    if not checked[i]:
        co += 1
print(co)
