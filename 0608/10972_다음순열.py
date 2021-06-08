import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().strip().split()))


boo = True
x = 0
for i in range(N-1,0,-1):
    if li[i] > li[i-1]:
        x=i-1
        break

for i in range(N-1,0,-1):
    if li[x] < li[i]:
        li[x], li[i] = li[i], li[x]
        li = li[:x+1] + sorted(li[x+1:])
        print(*li)
        boo = False
        break


if boo:
    print(-1)
