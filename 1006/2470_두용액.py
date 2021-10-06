import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().strip().split()))
solution.sort()


left, right = 0, N-1
sum_ = 2000000001

ans1, ans2 = left, right

while left < right:
    tmp = solution[left] + solution[right]
    if abs(tmp) < abs(sum_):
        ans1, ans2 = left, right
        sum_ = tmp
        if tmp == 0:
            break

    if tmp < 0:  # 음수 부분이 양수보다 크다 --> 오른쪽을 줄이면 어차피 더 작아짐, 왼쪽 음수부분을 늘려야함
        left += 1
    else:
        right -= 1

print(solution[ans1], solution[ans2])

# 시간 초과 -------------------------------------------
# for i in range(N):
#     for j in range(N-1, i, -1):
#         tmp = solution[i] + solution[j]
#         if sum_ > abs(tmp):
#             ans1, ans2 = i, j
#             sum_ = abs(tmp)
#         else:
#             if solution[j] < 0:
#                 break
#             else:
#                 continue
#     if sum_ == 0:
#         break
#     if solution[i] > 0:
#         break

# print(solution[ans1], end=' ')
# print(solution[ans2])
