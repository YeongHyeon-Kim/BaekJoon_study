import sys
from math import gcd
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    num = list(map(int, input().strip().split()))
    N = num[0]
    sum_gcd = 0
    for i in range(1,N+1):
        j = i
        while(j!=N):
            gcd_v = gcd(num[i],num[j+1])
            sum_gcd += gcd_v
            j+=1
    print(sum_gcd)


# def GCD(x,y):
#     while y:
#         x,y = y, x%y
#     return x