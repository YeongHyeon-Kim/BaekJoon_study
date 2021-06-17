import sys
from collections import defaultdict

input = sys.stdin.readline

N, M, V = map(int, input().strip().split())

graph = defaultdict(list)
for i in range(M):
    node1, node2 = map(int, input().strip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


for i in graph.keys():
    graph[i].sort()




def DFS(V):
    visited[V] = False
    print(V, end=' ')
    for i in graph[V]:
        if visited[i]:
            DFS(i)

def BFS(V):
    visited[V] = False
    queue = [V]
    while(queue):
        print(queue[0], end=' ')
        V = queue.pop(0)
        for i in graph[V]:
            if visited[i]:
                queue.append(i)
                visited[i] = False

visited = [True]*(N+1)
DFS(V)
print()
visited = [True]*(N+1)
BFS(V)