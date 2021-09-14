import sys
from collections import deque
input = sys.stdin.readline

N, S, M = map(int, input().strip().split())
V = list(map(int, input().strip().split()))

# 곡 개수의 행만큼 최대 볼륨값 까지의 열을 같는 배열 만들기
dp = [[False for _ in range(M+1)] for __ in range(N+1)]
dp[0][S] = True  # 맨 첫시작지점을 true로 바꿔서 시작하게 바꿔줌


for i in range(N):  # 시작부터 마지막곡 직전까지 for 문으로 돌아줌
    # 각 행의 모든 열 돌아줌 / 더하고 뺐을때 가능한 값이 여러개가 될 수 도 있으니 다 돌아준다.
    for j in range(M+1):
        check = dp[i][j]
        if check:  # 만약 전 행에서 가능한 값으로 바꿔줬던 인덱스 j 라면
            if j+V[i] <= M:  # j 는 현재 볼륨 --> 현재 볼륨에 더해서 max 값을 넘지 않는다면 가능한 볼륨 크기
                dp[i+1][j+V[i]] = True  # 현재볼륨 + 변화 가능 볼륨 값 인덱스를 true로 바꿔준다
            if j-V[i] >= 0:  # 현재 볼륨에 빼서 0보다 작지 않다면 가능한 볼륨 크기
                dp[i+1][j-V[i]] = True  # 현재볼륨 - 변화가능 볼륨 값 인덱스를 true로 바꿔준다.

for i in range(M, -1, -1):  # 가장 큰값을 찾을 거니까 마지막 인덱스부터 확인한다.
    if dp[N][i]:  # 만약 현재 i값의 dp 가 true 라면
        print(i)  # 가능한 max 값 출력
        break
else:  # for else 구문 / break 되지 않았다면 가능한 값이 하나도 없다는 뜻
    print(-1)


# # BFS 실패 --> 메모리초과 문제, 시간 초과
# start = deque([[S, 0]])
# result = 0
# #result = []
# while start:
#     tmp = start.popleft()
#     now, depth = tmp[0], tmp[1]

#     if depth == N:
#         result = max(result, now)
#         #result.append(now)
#     else:
#         now_change = V[depth]
#         new_depth = depth+1
#         minus_change = now-now_change
#         plus_change = now+now_change
#         if 0 <= minus_change <= M:
#             start.append([minus_change, new_depth])
#         if 0 <= plus_change <= M:
#             start.append([plus_change, new_depth])
# if result:
#     print(result)
#     #print(max(result))
# else:
#     print(-1)
