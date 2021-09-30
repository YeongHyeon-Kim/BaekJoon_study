import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
node_info = list(map(int, input().strip().split()))
del_node = int(input())

node = defaultdict(list)
for i in range(N):
    if node_info[i] != -1:
        node[node_info[i]].append(i)
    else:
        root = i
# 삭제
if del_node in node:
    for i in node[del_node]:
        if i in node:
            del node[i]
    del node[del_node]
for i in node:
    if del_node in node[i]:
        node[i].remove(del_node)

count = 0
visited = [False]*N

def DFS_count(child):
    global count
    if not node[child]:
        count += 1
        return
    else:
        for i in node[child]:
            if not visited[i]:
                visited[i] = True
                DFS_count(i)

if root in node:
    DFS_count(root)

print(count)


#유니온 파인드
# 같은 집합에 속하는건지