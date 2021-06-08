import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())

result = [0]*M
visited = [False]*N

def back(depth, N, M):
    if depth == M:
        print(str(result)[1:-1].replace(',',''))
        return
    else:
        for i in range(1,N+1):
            if not visited[i-1]:
                visited[i-1] = True
                result[depth] = i
                back(depth+1,N,M)
                visited[i-1] = False
back(0,N,M)

##permutation 사용하기
import itertools
p = list(itertools.permutations(N,M))
for value in p:
    print(' '.join(map(str, value)))
