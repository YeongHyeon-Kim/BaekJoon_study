import sys
import time
import copy
input=sys.stdin.readline

N, M = map(int,input().strip().split())

graph = [list(map(int,input().strip().split())) for i in range(N)]

visited = [[True]*M]*N

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def count_vi(graph,visited):
    #바이러스가 다 퍼졌을 때 0 개수 세아리기
    new_graph = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] ==2:
                new_graph[i][j] = 3
                
                queue = [[i,j]]
                while queue:
                    a, b = queue[0][0], queue[0][1]
                    del queue[0]
                    for k in range(4):
                        x = a+dx[k]
                        y = b + dy[k]
                        if  0<=x<N and 0<=y<M and new_graph[x][y] == 0:
                            new_graph[x][y] = 3
                            queue.append([x,y])
                        elif 0<=x<N and 0<=y<M and new_graph[x][y] == 2:
                            new_graph[x][y] = 3
                            queue.append([x,y])
    #바이러스인거 다 3으로 바꾼 후
    cnt = 0
    for i in range(N):
        cnt += new_graph[i].count(0)
    return cnt

cnt = 0
#벽 3개를 세우고 count하기


def setWall(start, depth):
    global cnt
    if depth ==3:
        cnt = max(cnt, count_vi(graph,visited))
        return
    
    for i in range(start, N*M):
        x = i //M
        y = i % M

        if graph[x][y] ==0:
            graph[x][y] = 1
            setWall(i+1,depth+1)
            graph[x][y] = 0


setWall(0,0)

print(cnt)





