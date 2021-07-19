import sys
input=sys.stdin.readline

N,M = map(int, input().strip().split())

def count2(num):
    cnt = 0
    while num != 0:
        num = num // 2
        cnt += num
    return cnt

def count5(num):
    cnt = 0
    while num != 0:
        num = num // 5
        cnt += num
    return cnt


print(min((count2(N)-count2(M)-count2(N-M)),(count5(N)-count5(M)-count5(N-M))))