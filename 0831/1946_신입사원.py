import sys
input=sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    volunteer = []
    for i in range(N):
        score = list(map(int ,input().strip().split()))
        volunteer.append(score)
    volunteer.sort(key = lambda x : x[0])
    min_access = volunteer[0][1]
    count = 1 # 1등은 무조건 뽑히니까
    for i in range(N):
        if min_access > volunteer[i][1]:
            count +=1
            min_access = volunteer[i][1]
    print(count)
