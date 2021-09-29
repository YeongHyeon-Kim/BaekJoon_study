import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

Y, X = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(Y)]
visited = [[False]*X for _ in range(Y)]
visited[0][0] = True

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def check_first(Y, X, y, x, now_time):
    global graph
    global visited
    next_ = deque()
    start = deque([[y, x]])
    while start:
        tmp = start.popleft()
        i, j = tmp[0], tmp[1]
        for k in range(4):
            near_x = j+dx[k]
            near_y = i+dy[k]
            if 0 <= near_x < X and 0 <= near_y < Y and not visited[near_y][near_x]:
                visited[near_y][near_x] = True
                if graph[near_y][near_x] == 0:
                    start.append([near_y, near_x])
                else:
                    next_.append([near_y, near_x, now_time])
    return next_


start = check_first(Y, X, 0, 0, 0)

count = [0]*max(Y//2, X//2)

before_time = 0


def after_hour(start):
    while start:
        tmp = start.popleft()
        now_y, now_x, now_time = tmp[0], tmp[1], tmp[2]
        count[now_time] += 1
        for i in range(4):
            near_x = now_x+dx[i]
            near_y = now_y+dy[i]
            if 0 <= near_x < X and 0 <= near_y < Y:
                if graph[near_y][near_x] == 1 and not visited[near_y][near_x]:  # 녹은 뒤 공기에 만날 부분
                    visited[near_y][near_x] = True
                    start.append([near_y, near_x, now_time+1])
                # 새로 생긴 구멍 확인 (원래 치즈 내부에 있었던 구멍)
                elif graph[near_y][near_x] == 0 and not visited[near_y][near_x]:
                    visited[near_y][near_x] = True
                    start.extend(check_first(Y, X, near_y, near_x, now_time+1))
    print(now_time+1)
    print(count[now_time])


after_hour(start)
