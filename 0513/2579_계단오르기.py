import sys
input = sys.stdin.readline

def solve(stairs, n):
    if n>3:
        result = []
        result.append(stairs[0])
        result.append(stairs[0]+stairs[1])
        result.append(max(stairs[2]+result[0],stairs[1]+stairs[2]))
        for i in range(3,n):
            ##max(2칸 전에서 올라온경우, 한칸전에서 올라온 경우)
            result.append(max(stairs[i]+result[i-2],stairs[i]+stairs[i-1]+result[i-3]))
        print(result[-1])
    else:
        print(sum(stairs))

N = int(input())
stairs=[]
for _ in range(N):
    stairs.append(int(input().strip()))

solve(stairs,N)
