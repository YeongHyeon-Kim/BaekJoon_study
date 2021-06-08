import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())
num = list(map(int,input().strip().split()))

sum_value = [0 for _ in range(N)]
for i in range(N):
    if i ==0:
        sum_value[i] = num[i]
    else:
        sum_value[i] = sum_value[i-1]+num[i]


for _ in range(M):
    i,j = map(int,input().strip().split())
    if i == 1:
        print(sum_value[j-1])
    else:
        pr = sum_value[j-1] - sum_value[i-2]
        print(pr)

