import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().strip().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False for _ in range(K)] for __ in range(N)]
visited[0][0] = True
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


dq = deque([[0, 0, 1]])
while dq:
    y, x, count = dq.popleft()
    if y == N-1 and x == K-1:
        print(count)
        break
    else:
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if 0 <= new_x < K and 0 <= new_y < N:
                if not visited[new_y][new_x] and maze[new_y][new_x] == 1:
                    dq.append([new_y, new_x, count+1])
                    visited[new_y][new_x] = True
