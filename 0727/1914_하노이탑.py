import sys
input=sys.stdin.readline


def count(N : int):
    print((2**N)-1)

def Nsmall(n : int,  a, b, c):
    if n == 1:
        print(a, c)
    else:
        Nsmall(n - 1, a, c, b)
        #
        print(a, c)
        #
        Nsmall(n - 1, b, a, c)


N = int(input())
if N <=20:
    count(N)
    Nsmall(N,1,2,3)
else:
    count(N)

