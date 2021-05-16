import sys
input = sys.stdin.readline

dic = {1:1,2:1,3:1,4:2,5:2}

def solve(dic,N):
    if N in dic:
        return dic[N]
    else:
        dic[N] = solve(dic,N-1) + solve(dic,N-5)
        return dic[N]


T = int(input())
for i in range(T):
    N = int(input())
    print(solve(dic,N))