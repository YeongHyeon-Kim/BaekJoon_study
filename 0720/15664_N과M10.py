import sys
input=sys.stdin.readline
N,M = map(int, input().strip().split())

su = sorted(list(map(int,input().strip().split())))

result = [0 for _ in range(M)]
visited = [False for _ in range(N)]
di = {}
def DFS(N,depth,M):
    if depth == M:
        s = ' '.join(map(str,result))
        if s not in di:
            di[s] = 1
            print(s)
    else:
        for i in range(N):
            if not visited[i]:
                if depth ==0:##depth가 0일때는 그냥 값 넣어주기만 하면 됨.
                    visited[i] = True
                    result[depth] = su[i]
                    DFS(N,depth+1,M)
                    visited[i] = False
                else:#depth가 0이 아닌순간부터 비내림차순이여야 하니까
                    if su[i] >= result[depth-1]: ## 방문안했는데 똑같은 수가 들어올 수도 있느니 >=으로 처리한다.
                        visited[i] = True
                        result[depth] = su[i]
                        DFS(N,depth+1,M)
                        visited[i] = False
                        result[depth] = 0
DFS(N,0,M)