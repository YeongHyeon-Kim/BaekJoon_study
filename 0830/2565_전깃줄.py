import sys
input=sys.stdin.readline

N = int(input())

list_AB = []
list_B = []
dp = [0 for _ in range(N)]
for i in range(N):
    list_AB.append(list(map(int, input().strip().split())))
list_AB.sort(key = lambda x : x[0])
for i in range(N):
    list_B.append(list_AB[i][1])
for i in range(N):
    for j in range(i):
        if list_B[i] > list_B[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(N - max(dp))