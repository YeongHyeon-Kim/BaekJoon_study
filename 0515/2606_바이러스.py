##깊이 우선 탐색 (DFS) 구현

import sys
input = sys.stdin.readline

Node = int(input())
line = int(input())

dic = {}
for i in range(Node):
    dic[i+1] = set()
for _ in range(line):
    k, v = map(int,input().strip().split())
    dic[k].add(v)
    dic[v].add(k)

def find(dic,infected):    
    for i in dic[infected]:
        if i not in check:
            check.append(i)
            find(dic,i)

check = []
find(dic,1)
print(len(check)-1)


