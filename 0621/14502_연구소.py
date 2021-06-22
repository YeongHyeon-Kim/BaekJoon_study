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
    return new_graph,cnt

cnt = 0
#벽 3개를 세우고 count하기
for i in range(N):
    for j in range(M):
        #첫번째 빈공간 발견, 벽세우기
        if graph[i][j] == 0 and visited[i][j]:
            visited[i][j] == False
            graph[i][j] = 1

            for i2 in range(N):
                for j2 in range(M):
                    #두번째 빈공간 발견, 벽세우기
                    if graph[i2][j2] == 0 and visited[i2][j2]:
                        visited[i2][j2] == False
                        graph[i2][j2] = 1
                        
                        for i3 in range(N):
                            for j3 in range(M):
                                #세번째 빈공간 발견, 벽세우기
                                if graph[i3][j3] == 0 and visited[i3][j3]:
                                    visited[i3][j3] = False
                                    graph[i3][j3] = 1
                                    
                                    new_graph,new_cnt = count_vi(graph,visited)
                                    
                                    if new_cnt > cnt:
                                        cnt = new_cnt
                                    
                                    #3번째 벽 해제
                                    visited[i3][j3] = True
                                    graph[i3][j3] = 0
                        #2번째 벽 해제
                        visited[i2][j2] = True
                        graph[i2][j2] = 0
        #첫번째 벽 해제, 방문은 False 그대로
            graph[i][j] = 0

print(cnt)





