import sys
import copy
input=sys.stdin.readline

N = int(input())

su = list(map(int, input().strip().split()))

result = copy.deepcopy(su)

for i in range(N):
    for j in range(i):
        if su[j] < su[i]:
            result[i] = max(result[i], result[j]+su[i])
print(max(result))

