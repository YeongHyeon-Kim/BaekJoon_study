# import sys
# input=sys.stdin.readline

# N = int(input())
# top = list(map(int,input().strip().split()))
# result = []
# for i in range(N-1,-1,-1):
#     for j in range(i-1,-1,-1):
#         if top[i] < top[j]:
#             result.append(j+1)
#             break
#     else:
#         result.append(0)

# print(*result[::-1])







N = int(input())  # 탑의 개수
top_list = list(map(int, input().split()))  # 탑 리스트
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > top_list[i]:  # 수신 가능한 상황 stack 마지막 탑(가장 가까운 탑)의 높이가 현재 탑높이보다 높을때
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
        answer.append(0)
    stack.append([i, top_list[i]])  # 인덱스, 값

print(" ".join(map(str, answer)))