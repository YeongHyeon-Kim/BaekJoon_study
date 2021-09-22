import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().strip().split())


cnt = 1
start = deque([[A, cnt]])
flag = True
while start:
    now, now_cnt = start.popleft()

    if now < 10**9:
        new1 = now*2
        new2 = (now*10)+1

        if new1 == B or new2 == B:
            print(now_cnt+1)
            flag = False
            break

        if new1 <= 10**9 and new1 < B:
            start.append([new1, now_cnt+1])
        if new2 <= 10**9 and new2 < B:
            start.append([new2, now_cnt+1])
if flag:
    print(-1)
