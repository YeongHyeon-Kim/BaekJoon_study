import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
li = list(map(int, input().strip().split()))
li.sort()
visited = [False]*N

result = [0]*M
def NandM(depth : int,N : int,M : int):
    if depth == M:
        print(*result)
        return
    else:
        for i in range(N):
            if not visited[i] and result[depth-1]<li[i]:
                visited[i] = True
                result[depth] = li[i]
                NandM(depth+1,N,M)
                visited[i] = False
                result[depth] = 0
                
NandM(0,N,M)
