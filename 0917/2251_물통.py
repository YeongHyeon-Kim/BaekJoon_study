import sys
from collections import deque

input = sys.stdin.readline

A, B, C = map(int, input().strip().split())

visitied = [[False for _ in range(A+1)] for __ in range(B+1)]
visitied[0][0] = True


def check(a, b):
    if not visitied[b][a]:
        visitied[b][a] = True
        queue.append([a, b])


queue = deque([[0, 0]])
ans = []


def BFS():
    while(queue):
        a, b = queue.popleft()
        c = C-a-b
        if a == 0:
            ans.append(c)
        # A->B
        pour = min(a, B-b)  # 다 옮길 것인지 / 그 전에 B가 가득차는지
        check(a-pour, b+pour)
        # B->A
        pour = min(b, A-a)
        check(a+pour, b-pour)
        # A->C
        pour = min(a, C-c)
        check(a-pour, b)
        # C->A
        pour = min(c, A-a)
        check(a+pour, b)
        # B->C
        pour = min(b, C-c)
        check(a, b-pour)
        # C->B
        pour = min(c, B-b)
        check(a, b+pour)
    ans.sort()
    print(*ans)


BFS()
