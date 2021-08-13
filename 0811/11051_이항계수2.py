import sys
input=sys.stdin.readline

N,K = map(int, input().strip().split())

def solve(N,K):
    result = 1
    for i in range(N,K,-1):
        result= (result)*(i)
    divide = 1
    for i in range(N-K,0,-1):
        divide = (divide)*(i)
    
    print((result//divide)%10007)

if K==0 or K==N:
    print(1)
else:
    solve(N,K)