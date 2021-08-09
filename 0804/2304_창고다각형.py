# import sys
# input=sys.stdin.readline

# N = int(input())

# jido = {}

# max_high = 0
# last_ind = 0
# for i in range(N-1):
#     ind, high = map(int, input().strip().split())
#     jido[ind] = high
#     max_high = max(high,max_high)
#     last_ind = max(ind,last_ind)


# jido = dict(sorted(jido.items(), key= lambda x : x[0]))

# # #시작점 받아오기
# # start_ind = jido[list(jido.keys())[0]]
# # before_high = jido[start_ind]

# big = 0
# max_flag = False
# start_flag = True

# for ind, high in jido.items():
#     if start_flag: #if 가 상수시간 이니까? 이게 더 빠른가?
#         before_ind = ind
#         before_high = high
#         start_flag = False
#     else:
#         if max_flag: #맥스가 이미 나옴 이제 낮은 값 찾아야함
#             a



#         else:#아직 맥스가 안나왔을때
#             if high == max_high: #현재 위치 --> 다음 값중에서 가장 높은값 찾기
#                 flag = True #이제 부터 작은값 찾을꺼
#                 big += high*(ind-before_ind)
#                 if ind == last_ind:
#                     big += high*1
#             # max를 아직 안만났을때는 
#             if before_high < high:
#                 big += high*(ind-before_ind)
#                 #ind 까지 넓이 구하고 이게 마지막인지 확인
#                 if ind == last_ind:
#                     big += high*1

import sys
input=sys.stdin.readline

N = int(input())

jido = {}

max_high = 0
last_ind = 0
for i in range(N):
    ind, high = map(int, input().strip().split())
    jido[ind] = high
    max_high = max(high,max_high)
    last_ind = max(ind,last_ind)

max_num = list(jido.values()).count(max_high)
jido = dict(sorted(jido.items(), key= lambda x : x[0]))

left_jido = {}
right_jido = {}

before_high=0
before_ind=0
big = 0
start_flag = True
max_flag = True
check_max = 0
last_max_ind = 0
first_max_ind = 0
#max 를 기준으로 좌 우 나누기
for ind, high in jido.items():
    if max_flag: # max 아직 안만남
        if high < max_high:
            if high >= before_high: # 전에꺼보다 낮은거는 필요없음
                left_jido[ind] = high
                before_high = high
        elif high == max_high: # 첫 max 만났을때
            first_max_ind = ind
            last_max_ind = ind
            big += max_high
            max_flag = False
            before_ind = ind
            check_max+=1
    else:
        if check_max == max_num:
            right_jido[ind] = high
        else:
            if high == max_high:
                big += high*(ind - before_ind)
                check_max+=1
                last_max_ind = ind
                before_ind = ind

before_ind = 0
before_high = 0
start_flag = True
for ind, high in left_jido.items():
    if start_flag: #if 가 상수시간 이니까? 이게 더 빠른가?
        before_ind = ind
        start_flag = False
        before_high = high
    else:
        big += before_high*(ind-before_ind)
        before_ind = ind
        before_high = high

big += before_high*(first_max_ind-before_ind)


right_jido = dict(sorted(right_jido.items(), key= lambda x : x[1],reverse=True))
before_ind = last_max_ind+1
start_flag = True
for ind, high in right_jido.items():
    if start_flag:
        if ind == last_ind:
            big += high*(ind+1-before_ind)
            break
        else:
            big += high*(ind+1-before_ind)
            before_ind = ind+1
            start_flag = False
    else:
        if ind == last_ind:
            big += high*(ind+1-before_ind)
            break
        else:
            big += high*(ind+1-before_ind)
            before_ind = ind+1
print(big)
