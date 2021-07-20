
input=sys.stdin.readline

A,B = map(int, input().split())

if A==B:
    print("1"*A)
elif A>B:
    print("1"*(A-B))
else:
    print("1"*(B-A))


####문제 자체를 모르겠음 이게 왜 최대공약수??????

import sys
from math import gcd
input=sys.stdin.readline

A,B = map(int, input().split())
a = gcd(A,B)
print('1'*a)