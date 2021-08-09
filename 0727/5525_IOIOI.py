#방법1 - 50점
# import sys
# input=sys.stdin.readline

# N= int(input())
# P = 'IOI'
# for i in range(1,N):
#     P += 'OI'

# M = int(input())
# S = list(input().strip())
# cnt = 0
# for i in range(M-len(P)):
#     if P == ''.join(S[i:i+len(P)]):
#         cnt+=1
# print(cnt)

#방법2 - 50점
# import sys
# from collections import deque
# input=sys.stdin.readline

# N= int(input())
# P = 'IOI'
# for i in range(1,N):
#     P += 'OI'

# M = int(input())
# S = deque(list(input().strip()))

# cnt=0
# new_P = ''
# for i in range(M):
#     if len(new_P) == len(P):
#         if new_P == P:
#             cnt+=1
#             new_P += S.popleft()
#             new_P = new_P[1:]
#         else:
#             new_P += S.popleft()
#             new_P = new_P[1:]
#     else:
#         new_P += S.popleft()

# print(cnt)


import sys
input=sys.stdin.readline

N= int(input())
P = 'IOI'
for i in range(1,N):
    P += 'OI'

M = int(input())
S = input().strip('O').strip()
fit_ = False
cnt = 0
before = ''
for s in S:
    #시작파트
    if before == s: #적합한 와중에 OO , II  처럼 조건에 맞지않는 부적합한게 나왔을때 밑에서 넘어가면 하나가 사라지니까 위에서도 확인
        fit_ = False
    if not fit_: #현재 조건에 적합하지 않은 상태로 빠져나와서 시작할때
        if s =='I': #시작이 I여야 조건 시작
            fit_ = True
            tmp = 1
            before = s
    #조건에 맞는중이라면
    else:#현재 조건에 적합함
        if before == s: #적합한 와중에 OO , II  처럼 조건에 맞지않는 부적합한게 나왔을때
            fit_ = False
        else:
            if s == 'I': #전에꺼는 O 이고 현재 나온게 I일때 --> IOI 처럼 조건에 적합
                tmp+=1
                before = s
                if tmp >= len(P):
                    cnt+=1
            else:
                tmp+=1
                before = s
#스위치는 O일때만 스위치 종료하면 


print(cnt)


