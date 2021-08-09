import sys
from collections import deque
input=sys.stdin.readline

#데이터 받기, min max 값 찾기
N = int(input())
jido = []
tmp_max = 0
tmp_min = 0
height = {0: 1}
for i in range(N):
    tmp = list(map(int,input().strip().split()))
    for j in tmp:
        if j not in height:
            height[j] = 1
    jido.append(tmp)

dx = [1,-1,0,0]
dy = [0,0,-1,1]
def BFS(jido, goal):
    visited = [[False for _ in range(N)] for __ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and jido[i][j]>goal:
                tmp = deque([[i,j]])
                while tmp:
                    i_, j_ = tmp[0][0], tmp[0][1]
                    del tmp[0]
                    for k in range(4):
                        new_i = dx[k] + i_
                        new_j = dy[k] + j_
                        if 0<= new_i < N and 0<= new_j < N and not visited[new_i][new_j] and jido[new_i][new_j] > goal:
                            tmp.append([new_i,new_j])
                            visited[new_i][new_j] = True
                cnt+=1
    return cnt

max_vv = -1
for i in height:#가장 작은거 +1부터 가장 큰거 -1까지 확인
    max_vv = max(BFS(jido,i),max_vv)
print(max_vv)