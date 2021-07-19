import sys
input=sys.stdin.readline

N = int(input())

box = list(map(int,input().strip().split()))

result = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if box[j] < box[i]:
            result[i] = max(result[j]+1,result[i])
print(max(result))