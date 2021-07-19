import sys
input=sys.stdin.readline

N, M = map(int, input().strip().split())
su = list(map(int, input().strip().split()))
su.sort()
visited = [False for i in range(N)]
result = [0 for i in range(M)]
check = True
def DFS(N,depth,M):
    if depth == M:
        print(*result)
        return
    overlap = 0
    #새로운 depth의 DFS로 들어오게 되면 값을 초기화 시켜줌
    for i in range(N):
        if not visited[i] and overlap != su[i]:
            #(depth+1 == M and result[M-1] == su[i]) and (check and ):##마지막값만 다르면 다른 수열
            visited[i] = True
            result[depth] = su[i]
            overlap = su[i]
            DFS(N,depth+1,M)
            #DFS 들어가기전의 overlap값이 남아 있어서 이 수가 바로 다음 for문에서 사용되는 것을 막아줌 
            visited[i] = False
DFS(N,0,M)