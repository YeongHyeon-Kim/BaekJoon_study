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

for i in coin[::-1]:
    
    if (i+now) <= K:
        
        tmp = (K-now)//i
        
        now += i*tmp
        
        cnt+= tmp

print(cnt)


#변수 줄여서 해보기