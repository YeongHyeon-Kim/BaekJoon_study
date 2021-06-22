import sys
input=sys.stdin.readline

N = int(input())

time = []
for i in range(N):
    start, end = map(int, input().strip().split())
    time.append([start,end])

time.sort(key = lambda a: a[0])
time.sort(key = lambda a: a[1])

cnt = 0
final_end = 0

for start, end in time:
    if start >= final_end:
        cnt+=1
        final_end = end

print(cnt)
