import sys
input = sys.stdin.readline

# 가장 긴 부분수열의 길이 찾기
N = int(input())
children = [int(input()) for _ in range(N)]

dp = [0 for _ in range(N)]


for i in range(N):
    for j in range(i):
        if children[i] > children[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(N - max(dp))
