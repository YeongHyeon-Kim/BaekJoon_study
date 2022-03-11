import sys
input = sys.stdin.readline

N = int(input())

i = 1
while 1:
    tmp = str(i)
    result = i
    for j in tmp:
        result += int(j)
    if(result == N):
        print(i)
        break
    if i >= N:
        print(0)
        break
    i += 1


N = int(input())

final_reuslt = 0
for i in range(1, N+1):
    result = sum(list(map(int, str(i))))
    result += i
    if(result == N):
        final_reuslt = i
        break
print(final_reuslt)
