T = int(input())

memo = {0:0,1:1,2:2,3:4}

def count(N):
    if N in memo:
        return memo[N]
    else:
        memo[N] = count(N-1) + count(N-2) + count(N-3)
        return memo[N]

for _ in range(T):
    N = int(input())
    print(count(N))