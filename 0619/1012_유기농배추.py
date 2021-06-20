import sys
input =sys.stdin.readline

T = int(input())

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = [[x,y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a+dx[i]
            w = b+dy[i]
            if 0<=q<N and 0<=w<M and ground[q][w] == 1:
                ground[q][w] = 0
                queue.append([q,w])


for i in range(T):
    #그래프 그리기
    M,N,K = map(int, input().strip().split())
    ground = [[0]*M for _ in range(N)]
    cnt = 0
    #배추 위치 받아오기
    for i in range(K):
        m,n = map(int, input().strip().split())
        ground[n][m] = 1

    for q in range(N):
        for w in range(M):
            if ground[q][w] == 1:
                bfs(q,w)
                ground[q][w] = 0
                cnt+=1

    print(cnt)
