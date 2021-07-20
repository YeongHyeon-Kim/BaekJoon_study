import sys

input=sys.stdin.readline

N,M = map(int,input().split())

su = list(set(map(int, input().strip().split())))
su.sort()
N = len(su)

result = [0 for i in range(M)]
def DFS(N,depth,M):
    if depth == M:
        print(*result)
    else:
        for i in range(N):
            result[depth] = su[i]
            DFS(N,depth+1,M)


DFS(N,0,M)
