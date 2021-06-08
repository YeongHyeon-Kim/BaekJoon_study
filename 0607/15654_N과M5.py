import sys
input = sys.stdin.readline

N,M = map(int, input().strip().split())

num = list(map(int,input().strip().split()))
num.sort()

check = [True]*N
pr = [0 for _ in range(M)]

def NandM(depth,N,M):
    if depth == M:
        print(str(pr)[1:-1].replace(',',''))
        return
    else:
        for i in range(N):
            if check[i]:
                check[i] = False
                pr[depth] = num[i]
                NandM(depth+1,N,M)
                check[i] = True

NandM(0,N,M)
