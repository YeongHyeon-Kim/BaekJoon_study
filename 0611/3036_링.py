import sys
from math import gcd
input = sys.stdin.readline

N = int(input())

li = list(map(int,input().strip().split()))

first_ling = li[0]

for i in range(1,N):
    GCD = gcd(first_ling,li[i])
    print(str(first_ling//GCD)+'/'+str(li[i]//GCD))