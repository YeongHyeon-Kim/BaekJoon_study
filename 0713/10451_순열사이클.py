import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

T = int(input())

def DFS(first, now):
    global cnt
    if now == first:
        cnt+=1
    else:
        visited[now-1] = True
        now = su[1][now-1]
        DFS(first,now)
        


for _ in range(T):
    N = int(input())
    su = [[i for i in range(1,N+1)]]
    su.append(list(map(int,input().strip().split())))

    visited = [False for __ in range(N)]
    cnt = 0
    for i in range(N):
        if not visited[i]:
            first = su[1][i]
            visited[first-1] = True
            DFS(first,su[1][first-1])
    print(cnt)
