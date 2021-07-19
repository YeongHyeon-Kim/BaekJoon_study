import sys
input=sys.stdin.readline

N = int(input())
map = []
for i in range(N):
    cost = list(map(int,input().strip().split()))
    map.append(cost)

