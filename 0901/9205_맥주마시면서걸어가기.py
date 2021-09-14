import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    start = deque([list(map(int, input().strip().split()))])
    stores_idx = []
    for __ in range(n):
        stores_idx.append(list(map(int, input().strip().split())))
    fes_x, fes_y = map(int, input().strip().split())
    flag = True
    # 데이터 받아오기 완료 flag - 도착 했으면 happy 출력 / 아니면 맨 밑 sad 출력

    visited = [False]*n
    while start:
        tmp = start.popleft()
        now_x, now_y = tmp[0], tmp[1]
        # 도착할수 있으면 , 맥주 한캔당 50 --> 맥주 20캔 --> 1000 만큼 갈수있음. / 편의점 들리면 초기화
        if abs((fes_y-now_y))+abs((fes_x-now_x)) <= 1000:
            print("happy")  # 편의점을 들렸다가 도착하던가, 맨 처음부터 도착 가능하던가 가능 하면 출력후 break
            flag = False
            break
        else:
            for i in range(n):
                # 편의점 들린곳 또 들릴 필요 없음 / 만약 그 편의점을 이미 들렸는데도 break가 안됐다는 말은 그 편의점을 통해서는 도착 불가
                if not visited[i]:
                    # 이미 그 편의점에서 도착할수 있는 편의점들은 queue에 추가된 상태
                    # 이 편의점에서 갈수있는 다른 편의점 찾기
                    if abs((stores_idx[i][1]-now_y))+abs((stores_idx[i][0]-now_x)) <= 1000:
                        start.append(stores_idx[i])  # 갈수있는 편의점은 모두 추가
                        visited[i] = True  # 한번 간 편의점은 다시 방문 안함.
    if flag:
        print("sad")
