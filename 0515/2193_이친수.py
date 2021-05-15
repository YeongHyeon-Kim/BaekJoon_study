import sys
input = sys.stdin.readline

N = int(input())

dic = {1:1,2:1,3:2}

def solve(dic, N):
    if N in dic:
        return dic[N]
    else:
        dic[N] = solve(dic,N-1) + solve(dic,N-2)
        return dic[N]

print(solve(dic,N))
