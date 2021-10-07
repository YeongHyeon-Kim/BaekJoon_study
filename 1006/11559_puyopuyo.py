from collections import deque
import sys
input = sys.stdin.readline


field = [list(map(str, input().strip())) for _ in range(12)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

dot = [[False for _ in range(6)] for __ in range(12)]

for i in range(12):
    for j in range(6):
        if field[i][j] == '.':
            dot[i][j] = True


def boom(boom_ind):
    global field
    global dot
    boom_ind.sort(key=lambda x: x[0])  # 높이를 기준으로 정렬 클수록 아래에 있는 뿌요
    for boom in boom_ind:
        x = boom[1]
        y = boom[0]
        for i in range(y, -1, -1):  # 한칸씩 밑으로 내리기
            if i == 0:
                field[i][x] = '.'
                dot[i][x] = True
            else:
                if field[i-1][x] == '.':
                    dot[i][x] = True
                field[i][x] = field[i-1][x]
    return True


boom_count = 0


def BFS(boom_count):
    global field
    global dot
    is_boom = False
    now_boom = []
    tmp_check = [[False for _ in range(6)] for __ in range(12)]
    for i in range(12):
        for j in range(6):
            if not dot[i][j]:
                tmp = deque([[i, j]])
                color = field[i][j]
                count = 1
                tmp_boom_ind = [[i, j]]
                tmp_check[i][j] = True
                while tmp:
                    y, x = tmp.popleft()
                    for k in range(4):
                        new_y = y + dy[k]
                        new_x = x + dx[k]
                        if 0 <= new_x < 6 and 0 <= new_y < 12 and not tmp_check[new_y][new_x]:
                            # 점이 아니고 같은 색이라면
                            if not dot[new_y][new_x] and color == field[new_y][new_x]:
                                tmp_check[new_y][new_x] = True
                                tmp.append([new_y, new_x])
                                tmp_boom_ind.append([new_y, new_x])
                                count += 1
                if count >= 4:  # 연쇄작용 발생
                    now_boom.extend(tmp_boom_ind)
    if now_boom:
        is_boom = boom(now_boom)
    if is_boom:
        boom_count += 1
    return boom_count


before_boom_count = 0
while True:
    after_boom_count = BFS(before_boom_count)
    if before_boom_count == after_boom_count:
        print(after_boom_count)
        break
    else:
        before_boom_count = after_boom_count

# 수정 필요 --> 한 타임에 모든 뿌요가 다 터지고 그 뒤에 뿌요가 내려오는것으로 봐야함
