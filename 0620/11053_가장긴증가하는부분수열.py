import sys
input = sys.stdin.readline

A = int(input())

su = list(map(int,input().strip().split()))
result = [0 for i in range(A)]

for i in range(A):
    for j in range(i):
        if su[i] > su[j] and result[i] < result[j]:
            result[i] = result[j]
    result[i] +=1

print(max(result))