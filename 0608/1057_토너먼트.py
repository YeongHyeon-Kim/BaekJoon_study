import sys
input = sys.stdin.readline

N,kim,im = map(int,input().strip().split())
cnt = 0

while(True):
    kim -= kim // 2
    im -= im // 2
    cnt+=1
    if kim == im:
        print(cnt)
        break