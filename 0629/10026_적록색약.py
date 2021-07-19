import sys
from copy import deepcopy
input=sys.stdin.readline

N = int(input())
grid = []

for i in range(N):
    grid.append(list(input().strip()))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def BFS_not(y,x,find_color,new_grid):
    queue = [[y,x]]
    while queue:
        y,x = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            new_y = y +dy[i]
            new_x = x +dx[i]
            if 0<=new_y<N and 0<=new_x<N and new_grid[new_y][new_x] == find_color:
                new_grid[new_y][new_x] = 'Y'
                queue.append([new_y,new_x])


new_grid = deepcopy(grid)
result = []
cnt = 0
for i in range(N):
    for j in range(N):
        if new_grid[i][j] =="R":
            BFS_not(i,j,"R",new_grid)
            cnt+=1
        elif new_grid[i][j] =="B":
            BFS_not(i,j,"B",new_grid)
            cnt+=1
        elif new_grid[i][j] =="G":
            BFS_not(i,j,"G",new_grid)
            cnt+=1
        else:
            pass
result.append(cnt)

for i in range(N):
    for j in range(N):
        if grid[i][j] =="G":
            grid[i][j] = "R"
cnt =0
for i in range(N):
    for j in range(N):
        if grid[i][j] =="R":
            BFS_not(i,j,"R",grid)
            cnt+=1
        elif grid[i][j] =="B":
            BFS_not(i,j,"B",grid)
            cnt+=1
        else:
            pass
result.append(cnt)

print(*result)



##파이썬 2등 코드
import sys

sys.setrecursionlimit(1000000)
a = int(sys.stdin.readline())
graphForNomal= [([0] * a) for _ in range(a)]
graphForRedGreen= [([0] * a) for _ in range(a)]
count_Nomal = 0
count_Red_Green = 0

for i in range(a) :
    str = sys.stdin.readline()
    for j in range(a) :
        graphForNomal[i][j] = str[j]
        if str[j] == "R" :
            graphForRedGreen[i][j] = "G"
        else :
            graphForRedGreen[i][j] = str[j]

def nomal_Dfs(graph, color, sero, garo) :
    if garo + 1 < a and (color == graph[sero][garo + 1]):
        graph[sero][garo + 1] = "A"
        nomal_Dfs(graph, color, sero, garo + 1)

    if sero + 1 < a and (color == graph[sero + 1][garo]) :
        graph[sero + 1][garo] = "A"
        nomal_Dfs(graph, color, sero + 1, garo)

    if garo - 1 > -1 and (color == graph[sero][garo - 1]) :
        graph[sero][garo - 1] = "A"
        nomal_Dfs(graph, color, sero, garo - 1)

    if sero - 1 > -1 and (color == graph[sero - 1][garo]) :
        graph[sero - 1][garo] = "A"
        nomal_Dfs(graph, color, sero - 1, garo)

#이거 필요 없을듯..?
'''
def red_Green_Dfs(color, sero, garo) :
    if garo + 1 < a and ()
'''

for i in range(a) :
    for j in range(a) :
        if graphForNomal[i][j] != "A" :
            temp = graphForNomal[i][j]
            graphForNomal[i][j] = "A"
            count_Nomal = count_Nomal + 1
            nomal_Dfs(graphForNomal, temp, i, j)

for i in range(a) :
    for j in range(a) :
        if graphForRedGreen[i][j] != "A" :
            temp = graphForRedGreen[i][j]
            graphForRedGreen[i][j] = "A"
            count_Red_Green = count_Red_Green + 1
            nomal_Dfs(graphForRedGreen, temp, i, j)

print(count_Nomal, end = ' ')
print(count_Red_Green)