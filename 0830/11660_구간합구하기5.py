# 당연히 시간초과
# import sys
# input=sys.stdin.readline


# N,M = map(int,input().strip().split())
# graph = []

# for i in range(N):
#     graph.append(list(map(int, input().strip().split())))

# for _ in range(M):
#     x1,y1,x2,y2 = map(int, input().strip().split())
#     result = 0
#     for i in range(x1-1,x2):
#         for j in range(y1-1,y2):
#             result += graph[i][j]
    
#     print(result)

#또 시간초과
# import sys, copy
# input=sys.stdin.readline


# N,M = map(int,input().strip().split())
# graph = [list(map(int, input().strip().split())) for _ in range(N)]

# sum_graph = copy.deepcopy(graph)

# for i in range(N):
#     for j in range(N):
#         if i ==0 and j ==0:
#             pass
#         elif i ==0:
#             sum_graph[i][j] += sum_graph[i][j-1]
#         elif j ==0:
#             sum_graph[i][j] += sum_graph[i-1][j]
#         else:
#             sum_graph[i][j] += (sum_graph[i-1][j] + sum(graph[i][:j])) # 윗줄 앞까지의 합 + 아래줄 원래 값들의 합

# for i in range(M):
#     x1,y1,x2,y2 = map(int, input().strip().split())
#     if x1 ==1 and y1 == 1: ## 첨부터 ~
#         print(sum_graph[x2-1][y2-1])
#     elif x1 ==1 :
#         print(sum_graph[x2-1][y2-1] - sum_graph[x2-1][y1-2])
#     elif y1 ==1:
#         print(sum_graph[x2-1][y2-1] - sum_graph[x1-2][y2-1])
#     else:
#         print(sum_graph[x2-1][y2-1] - sum_graph[x2-1][y1-2] - sum_graph[x1-2][y2-1] + sum_graph[x1-2][y1-2] )


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0 for i in range(n + 1)] for i in range(n + 1)]
s = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + s[i][j]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - (dp[x1 - 1][y2] + dp[x2][y1 - 1] - dp[x1 - 1][y1 - 1]))