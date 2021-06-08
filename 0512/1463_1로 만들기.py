# #DP

# N = int(input())

# dp = [0 for _ in range(N+1)]

# for i in range(2, N+1): #1은 바로 1이여서 0이기 때문에 for문은 2부터 시작한다.
#     dp[i] = dp[i-1]+1
    
#     if i%2==0 and dp[i//2]+1 < dp[i]:
#         dp[i] = dp[i//2]+1
    
#     if i%3==0 and dp[i//3]+1 < dp[i]:
#         dp[i] = dp[i//3]+1
    
# print(dp[N])

# 연산이 2번  if min max 
#DP

#바꾼 코드 연산이 줄어든다.
N = int(input())

dp = [0 for _ in range(N+1)]

for i in range(2, N+1): #1은 바로 1이여서 0이기 때문에 for문은 2부터 시작한다.
    dp[i] = dp[i-1]+1
    
    di2 = dp[i//2]+1
    if i%2==0 and  di2 < dp[i]:
        dp[i] = di2
    
    di3 = dp[i//3]+1
    if i%3==0 and di3 < dp[i]:
        dp[i] = di3
    
print(dp[N])
