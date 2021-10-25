import sys
from collections import deque
input = sys.stdin.readline

S = int(input())


def BFS():
    clipboard = deque([[1, 0]])  # 화면, 클립보드
    time = 0
    while clipboard:
        now = clipboard.popleft()
        if now == S:
            print(time)
            return

        else:
