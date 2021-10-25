import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for __ in range(M)]
visited = [[False for _ in range(N)] for __ in range(M)]

tomato = deque()
count = N*M
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            tomato.append([i, j])
            visited[i][j] = True
            count -= 1
        elif graph[i][j] == -1:
            count -= 1
            visited[i][j] = True


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(tomato):
    global count
    new_tomato = deque()
    while tomato:
        y, x = tomato.popleft()
        for i in range(4):
            new_y = y+dy[i]
            new_x = x+dx[i]
            if 0 <= new_y < M and 0 <= new_x < N:
                if not visited[new_y][new_x]:
                    if graph[new_y][new_x] == 0:
                        graph[new_y][new_x] = 1
                        visited[new_y][new_x] = True
                        new_tomato.append([new_y, new_x])
                        count -= 1
    return new_tomato


day = 0
while count != 0:
    tomato = BFS(tomato)
    day += 1
    if len(tomato) == 0:
        print(-1)
        break
else:
    print(day)
