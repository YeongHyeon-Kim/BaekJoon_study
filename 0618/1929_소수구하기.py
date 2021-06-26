import sys
input = sys.stdin.readline

M,N = map(int, input().strip().split())


def isPrime(M,N):
    check = [True] * (N+1)
    check[1] = False
    m = int(N**0.5)
    for i in range(2,m+1):
        if check[i]:
            for j in range(i+i, N+1, i):
                check[j] = False
    return [i for i in range(M, N+1) if check[i]== True]

sosu = isPrime(M,N)
for i in range(len(sosu)):
    print(sosu[i])
