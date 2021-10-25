import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False for _ in range(N)] for __ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(point: deque):
    global visited
    count = 1
    while point:
        y, x = point.popleft()
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if 0 <= new_x < N and 0 <= new_y < N:
                if not visited[new_y][new_x] and graph[new_y][new_x] == 1:
                    count += 1
                    visited[new_y][new_x] = True
                    point.append([new_y, new_x])
                elif graph[new_y][new_x] == 0:
                    visited[new_y][new_x] = True
    return count


result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if graph[i][j] == 0:
                visited[i][j] = True
            else:
                visited[i][j] = True
                result.append(BFS(deque([[i, j]])))
result = sorted(result)
print(len(result))
if result:
    for i in result:
        print(i)
else:
    print(0)
