import sys
from math import gcd
input = sys.stdin.readline

a1,b1 = map(int, input().strip().split())
a2,b2 = map(int, input().strip().split())

B = b1*b2
A = b1*a2 + b2*a1
GCD = gcd(A,B)

B = int(B/GCD)
A = int(A/GCD)

print(B, end=' ')
print(A)
