import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
cards = deque([i for i in range(1, N+1)])

while len(cards) != 1:
    cards.popleft()
    cards.rotate(-1)

print(cards.pop())
