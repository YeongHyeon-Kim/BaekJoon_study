import sys
input=sys.stdin.readline

pan = [list(map(str, input().strip().split())) for _ in range(5)]

dx= [1,-1,0,0]
dy = [0,0,-1,1]
Dic = {}
cnt = 0
def DFS(x,y,num):
    global cnt
    if len(num) == 6:
        if num not in Dic:
            Dic[num] = 1
            cnt+=1
    else:
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if 0<=new_x < 5 and 0<=new_y <5:
                DFS(new_x,new_y,num+pan[new_x][new_y])

for i in range(5):
    for j in range(5):
        DFS(i,j,pan[i][j])
print(cnt)