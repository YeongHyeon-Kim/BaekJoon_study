from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

graph = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for __ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

painting_num = 0
max_area = 0


def BFS(y, x):
    q = deque([[x, y]])
    now_area = 0
    while q:
        now_area += 1
        now_x, now_y = q.popleft()
        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]
            if 0 <= new_x < m and 0 <= new_y < n:
                if not visited[new_y][new_x]:
                    visited[new_y][new_x] = True
                    if graph[new_y][new_x] == 1:
                        q.append([new_x, new_y])
    return now_area


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            max_area = max(BFS(i, j), max_area)
            painting_num += 1

print(painting_num)
print(max_area)
