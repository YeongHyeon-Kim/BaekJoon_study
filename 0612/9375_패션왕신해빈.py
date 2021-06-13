import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    result = {}
    for __ in range(n):
        name, kind = input().strip().split()
        if kind in result:
            result[kind] +=1
        else:
            result[kind] = 1
    final = 1
    for i in result.keys():
        final *= result[i]+1
    print(final-1)
