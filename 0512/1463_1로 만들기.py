#DP

N = int(input())

dp = [0 for _ in range(N+1)]

for i in range(2, N+1): #1은 바로 1이여서 0이기 때문에 for문은 2부터 시작한다.
    dp[i] = dp[i-1]+1
    
    if i%2==0 and dp[i//2]+1 < dp[i]:
        dp[i] = dp[i//2]+1
    
    if i%3==0 and dp[i//3]+1 < dp[i]:
        dp[i] = dp[i//3]+1
    
print(dp[N])