# import sys
# input=sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     volunteer = []
#     for i in range(N):
#         score = list(map(int ,input().strip().split()))
#         volunteer.append(score)
#     volunteer.sort(key = lambda x : x[0])
#     min_access = volunteer[0][1]
#     count = 1 # 1등은 무조건 뽑히니까
#     for i in range(N):
#         if min_access > volunteer[i][1]:
#             count +=1
#             min_access = volunteer[i][1]
#     print(count)


#굳이 []로 넣을 필요가 없음 score
import sys
input=sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    volunteer = [0 for _ in range(N+1)]
    for i in range(N):
        paper, inter = map(int, input().split())
        volunteer[paper] = inter
    min_access = volunteer[1]
    count = 1 # 1등은 무조건 뽑히니까
    for i in range(2,N+1):
        if min_access > volunteer[i]:
            count +=1
            min_access = volunteer[i]
    print(count)