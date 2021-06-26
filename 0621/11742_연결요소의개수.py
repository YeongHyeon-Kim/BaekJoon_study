import sys
from collections import defaultdict
input=sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)



graph = defaultdict(list)

N,M = map(int,input().strip().split())
visited = [False]*(N+1) 

for i in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        count+=1
print(count)