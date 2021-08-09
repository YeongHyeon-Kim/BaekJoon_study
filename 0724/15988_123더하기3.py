import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

T = int(input())

memo = [0 for i in range(1000001)]
memo[0] = 1
memo[1] = 1
memo[2] = 2
memo[3] = 4

for i in range(4,1000001):
    memo[i] = memo[i-1]%1000000009 + memo[i-2]%1000000009 + memo[i-3]%1000000009


# def solve(n):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = solve(n-1) + solve(n-2) + solve(n-3)
#         return memo[n]

for _ in range(T):
    n = int(input())
    print(memo[n]%1000000009)
    
    # if n in memo:
    #     print(memo[n])
    # else:
    #     memo[n] = solve(n)
    #     print(memo[n])
