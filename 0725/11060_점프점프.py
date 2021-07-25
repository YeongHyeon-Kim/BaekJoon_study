import sys
input=sys.stdin.readline

N = int(input())
su = list(map(int, input().strip().split()))
result = [N+1 for _ in range(N)]
result[0] = 0
for i in range(N):
    ra = su[i] +1
    for j in range(1, ra):
        if i+j <N:
            result[i+j] = min(result[i]+1, result[i+j])
        else:
            break

if result[-1] != N+1:
    print(result[-1])
else:
    print(-1)