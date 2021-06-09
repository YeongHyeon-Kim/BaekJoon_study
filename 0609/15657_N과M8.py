import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
li = list(map(int, input().strip().split()))
li.sort()

result = [0]*M

def NandM(depth,N,M):
    if depth == M:
        print(*result)
    else:
        for i in range(N):
            if result[depth-1] <= li[i]:
                result[depth] = li[i]
                NandM(depth+1,N,M)
                result[depth] = 0

NandM(0,N,M)