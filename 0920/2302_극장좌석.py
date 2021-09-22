import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
vip = [int(input()) for _ in range(M)]

possible = [1]*41
for i in range(2, 41):
    possible[i] = possible[i-1]+possible[i-2]

seat = []
tmp = []
for i in range(1, N+1):
    if i not in vip:
        tmp.append(i)
    else:
        seat.append(tmp)
        tmp = []
seat.append(tmp)

ans = 1
for i in range(len(seat)):
    length = len(seat[i])
    ans *= possible[length]
print(ans)
