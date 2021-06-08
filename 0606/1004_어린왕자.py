import sys
import math
input = sys.stdin.readline

T = int(input())

for i in range(T):
    cnt = 0
    x1,y1,x2,y2 = map(int,input().strip().split())
    n = int(input())
    for i in range(n):
        cx,cy,r = map(int,input().strip().split())

        tmp_r1 = (cx-x1)**2 + (cy-y1)**2
        tmp_r2 = (cx-x2)**2 + (cy-y2)**2
        new_r = r**2

        if (tmp_r1 < new_r and tmp_r2 > new_r) or (tmp_r1 > new_r and tmp_r2 < new_r):
            cnt+=1
    
    print(cnt)