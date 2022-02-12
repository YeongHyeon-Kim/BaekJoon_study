import sys
input = sys.stdin.readline

K, N = map(int, input().strip().split())

lan = []
for i in range(K):
    lan.append(int(input()))

max_lan = max(lan)
start = 1


def calc(length):
    sum = 0
    for i in lan:
        sum += i//length
    return sum


result = 0
while(start <= max_lan):
    mid = (max_lan+start) // 2
    count = calc(mid)
    if count < N:
        max_lan = mid - 1
    else:
        result = max(result, mid)
        start = mid + 1

print(result)
