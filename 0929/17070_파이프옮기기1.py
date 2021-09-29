# import sys
# input = sys.stdin.readline

# N = int(input())
# graph = [list(map(int, input().strip().split())) for _ in range(N)]


import sys


def check(y, x, d):
    for direction in directions[d]:
        dy, dx = cos[direction]
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < n and not g[ny][nx]:
            if direction != 2:  # 대각선이 아니면
                dp[ny][nx][direction] += dp[y][x][d]
            else:  # 대각선이면
                if not g[ny-1][nx] and not g[ny][nx-1]:
                    dp[ny][nx][direction] += dp[y][x][d]


directions = {0: [0, 2], 1: [1, 2], 2: [0, 1, 2]}
# 가로(0) / 세로(1) / 대각선(2)
cos = {0: [0, 1], 1: [1, 0], 2: [1, 1]}  # (y, x)
n = int(sys.stdin.readline().strip())
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
g = []
for _ in range(n):
    g.append([int(x) for x in sys.stdin.readline().split()])
dp[0][1][0] = 1
for y in range(n):
    for x in range(n):
        for d in range(3):
            if dp[y][x][d] and not g[y][x]:
                check(y, x, d)
print(sum(dp[n-1][n-1]))


# 아무리 봐도 아님... 이 방법은 포기
# check = [[[False]*3 for _ in range(N)] for __ in range(N)]
# check[0][1][2] = True

# count = [[0 for i in range(N)] for j in range(N)]
# count[0][1] = 1


# def check_right(y, x):
#     global check
#     global graph
#     if x+1 == N-1 and y == N-1:
#         if graph[y][x+1] == 0:
#             count[y][x+1] += count[y][x]

#     else:
#         if x+2 < N and graph[y][x+1] == 0 and graph[y][x+2] == 0:
#             check[y][x+1][2] = True
#             count[y][x+1] += count[y][x]


# def check_bottom(y, x):
#     global check
#     global graph
#     if x == N-1 and y+1 == N-1:
#         if graph[y+1][x] == 0:
#             count[y+1][x] += count[y][x]
#     else:
#         if y+2 < N and graph[y+1][x] == 0 and graph[y+2][x] == 0:
#             check[y+1][x][1] = True
#             count[y+1][x] += count[y][x]


# def check_diagonal(y, x):
#     global check
#     global graph
#     if x+1 < N and y+1 < N:
#         if graph[y+1][x+1] == 0 and graph[y+1][x] == 0 and graph[y][x+1] == 0:
#             check[y+1][x+1][0] = True
#             count[y+1][x+1] += count[y][x]


# def _check(y, x):
#     global check
#     global graph
#     for i in range(3):
#         if check[y][x][i]:
#             if i == 0:  # 가로에서 오기 가능
#                 check_right(y, x)
#                 check_bottom(y, x)
#                 check_diagonal(y, x)
#                 # 옆으로
#             elif i == 1 and not check[y][x][0]:  # 세로에서 오기 가능
#                 check_diagonal(y, x)
#                 check_bottom(y, x)
#             elif i == 2 and not check[y][x][0]:  # 대각선에서 오기 가능
#                 check_right(y, x)
#                 check_diagonal(y, x)


# for i in range(N):
#     for j in range(1, N):
#         if graph[i][j] != 1:
#             _check(i, j)

# print(count)
