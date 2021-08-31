import sys
from copy import deepcopy
input=sys.stdin.readline

M, N, H = map(int,input().strip().split())

box = []
start = []
goal_cnt = 0
for i in range(H):
    tmp = []
    for j in range(N):
        tmp_tmp = list(map(int, input().strip().split()))
        for k in range(M):
            if tmp_tmp[k] == 1:
                start.append([i,j,k])
            elif tmp_tmp[k] == 0:
                goal_cnt+=1
        tmp.append(tmp_tmp)
    box.append(tmp)

height = [0,1,-1]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

check_cnt = 0
day = 0
## while 2개로 바꿔보기
def BFS(start,box):
    global check_cnt
    global day
    new_start = []
    while start:
        i,j,k = start[0][0], start[0][1], start[0][2]
        del start[0]
        for i_ in range(3):
            if i_==0:
                for j_ in range(4):
                    new_j = j + dx[j_]
                    new_k = k + dy[j_]
                    if 0<=new_j<N and 0<=new_k<M and box[i][new_j][new_k] == 0:
                            box[i][new_j][new_k] = 1
                            check_cnt +=1
                            new_start.append([i,new_j,new_k])
            else:
                new_i = i + height[i_]
                if 0<=new_i<H and box[new_i][j][k] == 0:
                    box[new_i][j][k] = 1
                    check_cnt +=1
                    new_start.append([new_i,j,k])
    start = new_start.copy()
    if len(start) != 0:
        day +=1
        BFS(start,box)

if goal_cnt == 0:
    print(0)
else:
    BFS(start,box)
    if goal_cnt != check_cnt:
        print(-1)
    else:
        print(day)