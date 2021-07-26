import sys
from collections import deque
input=sys.stdin.readline

R,C = map(int, input().split())
map_ = [0 for _ in range(R)]
for i in range(R):
    map_[i] = list(input().strip())

visited = [[False for _ in range(C)] for __ in range(R)]
dx = [1,-1,0,0,0]
dy = [0,0,-1,1,0]

def check_out(i,j):
    tmp = deque([[i,j]])
    while tmp:
        new_x, new_y = tmp.popleft()
        for i in range(5):
            new_x += dx[i]
            new_y += dy[i]
            if 0<=new_x<R-1 and 0<=new_y<C-1 and not visited[new_x][new_y] and map_[new_x][new_y] == '.':
                visited[new_x][new_y] = True
                tmp.append([new_x,new_y])

def count_sw(i,j):
    sheep = 0
    wolf = 0
    tmp = deque([[i,j]])
    while tmp:
        x, y = tmp.popleft()
        for i in range(5):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0<=new_x<R-1 and 0<=new_y<C-1:
                if not visited[new_x][new_y]:
                    if map_[new_x][new_y] == 'o':
                        sheep +=1
                        visited[new_x][new_y] = True
                        tmp.append([new_x,new_y])
                    elif map_[new_x][new_y] == 'v':
                        wolf +=1
                        visited[new_x][new_y] = True
                        tmp.append([new_x,new_y])
                    else:
                        visited[new_x][new_y] = True
                        tmp.append([new_x,new_y])
    if sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf

#탈출, 울타리 visited 처리하기
for i in range(R):
    for j in range(C):
        if map_[i][j] == '#':
            visited[i][j] = True
        if (i == 0 or i == R-1) and not visited[i][j]:
            visited[i][j] = True
            check_out(i,j)
        elif (j==0 or j == C-1) and not visited[i][j]:
            visited[i][j] = True
            check_out(i,j)

sheep, wolf = 0,0
for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            new_sheep, new_wolf = count_sw(i,j)
            sheep += new_sheep
            wolf += new_wolf

print(sheep)
print(wolf)
