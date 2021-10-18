import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().strip().split())


def BFS(N, K):
    tmp = deque([N])
    count = [[-1, 0] for _ in range(100001)]
    count[N][0] = 0
    count[N][1] = 1
    while tmp:
        now = tmp.popleft()
        for i in [now+1, now-1, now*2]:
            if 0 <= i <= 100000:
                if count[i][0] == -1:  # 첫방문
                    count[i][0] = count[now][0]+1  # 시간 +1
                    count[i][1] = count[now][1]  # 주소값 연결로
                    tmp.append(i)
                elif count[i][0] == count[now][0]+1:  # 다시 방문했을때
                    count[i][1] += count[now][1]
    print(count[K][0])
    print(count[K][1])


if N >= K:
    print(N-K)
    print(1)
else:
    BFS(N, K)
