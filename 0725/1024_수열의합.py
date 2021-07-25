import sys
input=sys.stdin.readline

N,L = map(int, input().strip().split())

t= 0
x = -1
iter = 0

for i in range(L,101): #최소 길이부터 최대 길이까지
    t = (i*i-i) / 2
    if (N-t)% i ==0 and (N-t)//i >= 0: #딱 나누어 떨어지고 시작점이 0보다 크거나 같다.
        x = (N-t)//i
        iter = i
        break

if x == -1:
    print(-1)
else:
    for i in range(iter):
        if i != iter-1:
            print(int(x+i), end=' ')
        else:
            print(int(x+i))