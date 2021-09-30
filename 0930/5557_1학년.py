import sys
input = sys.stdin.readline

N = int(input())
num_li = list(map(int, input().strip().split()))


result = [[0]*21 for _ in range(N-1)]  # 아는 수가 0~20까지
result[0][num_li[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if result[i-1][j]:
            if 0 <= j+num_li[i] <= 20:
                result[i][j+num_li[i]] += result[i-1][j]
            if 0 <= j-num_li[i] <= 20:
                result[i][j-num_li[i]] += result[i-1][j]
print(result[-1][num_li[-1]])


# 문제 잘못읽음,,, 숫자 20까지밖에 모른다는 것은 숫자 2개를 합칠 수 있다는게 아니라 그냥 20까지밖에 모름
# 모든 수 사이사이에 +- 가 들어가야 함.
# for i in range(1, N-1):
#     for j in result[i-1]:
#         if i < N-2:
#             if num_li[i] != 0:
#                 compare_2 = (num_li[i]*10 + num_li[i+1])
#                 if compare_2 <= 20:
#                     result[i+1].append(compare_2 + j)
#                     if j >= compare_2:  # 음수가 아닐때
#                         result[i+1].append(j - compare_2)
#             sum_ = num_li[i]+j
#             if sum_ <= 20:
#                 result[i].append(sum_)
#             if j >= num_li[i]:
#                 result[i].append(j - num_li[i])
#         else:
#             if num_li[i]+j == goal:
#                 count += 1
#             if j - num_li[i] == goal:
#                 count += 1

# print(count)
