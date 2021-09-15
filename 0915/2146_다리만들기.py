import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip().split())) for i in range(N)]
visited = [[False for _ in range(N)] for __ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def change_island_num(start, num):  # 섬별로 번호를 바꿔줌
    while start:
        x, y = start.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # 방문하지 않았고, 값이 1인 점 바꾸기
            if 0 <= new_x < N and 0 <= new_y < N and graph[new_y][new_x] and not visited[new_y][new_x]:
                graph[new_y][new_x] = num
                visited[new_y][new_x] = True
                start.append([new_x, new_y])


num = 1
for y in range(N):
    for x in range(N):
        if graph[y][x] and not visited[y][x]:
            graph[y][x] = num
            change_island_num(deque([[x, y]]), num)
            num += 1


def find_min_dist(num):
    global min_value
    dist = [[-1 for _ in range(N)]for __ in range(N)]  # 0이랑 구별하기 위해서 -1로 해줌

    island = deque()
    for y in range(N):
        for x in range(N):
            if graph[y][x] == num:
                dist[y][x] = 0  # 시작점 거리 0으로 바꿔주기
                island.append([x, y])  # 현재 섬의 위치 모두 찍어두기

    while island:
        x, y = island.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if graph[new_y][new_x] > 0 and graph[new_y][new_x] != num:  # 바다가 아니고, 현재 섬이 아니라면
                    min_value = min(min_value, dist[y][x])
                    return  # 일단 다른섬에 도착하면 바로 끝 / BFS니까 가장 먼저 도착한게 앞에 queue에 있을테니까

                # graph[new_y][new_x]==0(바다), 아직 다리가 이어지지 않은부분 -1 이상이면
                elif graph[new_y][new_x] == 0 and dist[new_y][new_x] == -1:
                    # 전 거리에서 더하기 1 / 육지에서 시작하니까 1부터 시작할거임
                    dist[new_y][new_x] = dist[y][x] + 1
                    island.append([new_x, new_y])


min_value = 99999999999999999999999999999
for i in range(1, num):
    find_min_dist(i)
print(min_value)
