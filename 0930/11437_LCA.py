# import sys
# from collections import defaultdict
# input=sys.stdin.readline

# N = int(input())
# node = defaultdict(list)
# for _ in range(N):
#     a,b = map(int, input().strip().split())
#     node[a].append(b)


import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(cur, d):
    depth[cur] = d
    visited[cur] = True

    for child in tree[cur]:
        if not visited[child]:
            parent[child][0] = cur  # 바로 위 부모 [0]에 저장
            dfs(child, d+1)


def find_parent():
    for i in range(1, 21):
        for j in range(1, V+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]  # 부모 위의 부모 찾기


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(20, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return b

    for i in range(20, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

depth = [0] * (V+1)
parent = [[0 for _ in range(21)] for _ in range(V+1)]
visited = [False] * (V+1)


dfs(1, 0)
find_parent()
M = int(input())
for _ in range(M):
    A, B = map(int, input().split())
    common_parent = lca(A, B)
    print(common_parent)
