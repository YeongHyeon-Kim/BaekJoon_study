import sys
from collections import deque

input=sys.stdin.readline

N,M,K,X = map(int, input().strip().split())
jido = {}
for i in range(1,N+1):
    jido[i] = []
visited = [False for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().strip().split())
    jido[A].append(B)

def BFS(depth : int, K : int, X: int):
    result = []
    tmp = deque([X])
    visited[X] = True
    while tmp:
        if depth == K:
            for i in tmp: ##sort 를 미리 하는게 더 손해? 라고 생각해서 result 에 넣고 나중에 최종결과에서 sort
                result.append(i)
            return result
        else:
            tmp_next = []
            for i in tmp:
                for j in jido[i]:
                    if not visited[j]:
                        visited[j] = True
                        tmp_next.append(j)
            depth+=1
            tmp = tmp_next
    print(-1)
    return
re = BFS(0,K,X)
if re:
    re.sort()
    for i in re:
        print(i)