import sys
input=sys.stdin.readline
N = int(input())

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        #
        print(a, c)
        #
        hanoi(n - 1, b, a, c)
        #
cnt = 1
for i in range(N-1):
    cnt = cnt*2+1
print(cnt)
hanoi(N, 1, 2, 3)