import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().strip().split())


coin=[]
for i in range(N):
    new = int(input())
    if new <= K:
        coin.append(new)

now = 0
cnt = 0

for i in range(len(coin)-1,-1,-1):
    if (coin[i]+now) <= K:
        tmp = (K-now)//coin[i]
        now += coin[i]*tmp
        cnt+= tmp

print(cnt)
