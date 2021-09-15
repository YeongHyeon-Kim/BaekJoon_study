import sys
input = sys.stdin.readline


# N, M, K = map(int, input().strip().split())

# # 테이블 2개 만들꺼임
# k_row = K//M
# k_col = K % M

# table = [[0 for _ in range(k_col)] for __ in range(k_row+1)]
# for i in range(k_row+1):
#     for j in range(k_col):
#         if i == 0 or j == 0:
#             table[i][j] = 1
#         else:
#             table[i][j] = table[i][j-1] + table[i-1][j]

# if table[0]:
#     before_k = table[-1][-1]
# else:
#     before_k = 1

# if k_col == 0:
#     table = [[0 for _ in range(k_col, M)] for __ in range(k_row, N)]
# else:
#     table = [[0 for _ in range(k_col, M+1)] for __ in range(k_row, N)]

# for i in range(N-k_row):
#     if k_col == 0:
#         length = M-k_col
#     else:
#         length = M-k_col+1
#     for j in range(length):
#         if i == 0 or j == 0:
#             table[i][j] = 1
#         else:
#             table[i][j] = table[i][j-1] + table[i-1][j]
# if table[0]:
#     after_k = table[-1][-1]
# else:
#     after_k = 1
# print(before_k*after_k)


# N, M, K = map(int, input().strip().split())

# table = [[0 for _ in range(M)] for __ in range(N)]
# if K == 0:
#     for i in range(N):
#         for j in range(M):
#             if i == 0 or j == 0:
#                 table[i][j] = 1
#             else:
#                 table[i][j] = table[i][j-1] + table[i-1][j]
#     print(table[-1][-1])
# else:
#     k_row = K//M
#     k_col = K % M

# # 테이블 2개 만들꺼임
#     table = [[0 for _ in range(k_col)] for __ in range(k_row+1)]
#     for i in range(k_row+1):
#         for j in range(k_col):
#             if i == 0 or j == 0:
#                 table[i][j] = 1
#             else:
#                 table[i][j] = table[i][j-1] + table[i-1][j]
#     before_k = table[-1][-1]

#     table = [[0 for _ in range(k_col, M+1)] for __ in range(k_row, N)]
#     for i in range(N-k_row):
#         for j in range(M-k_col+1):
#             if i == 0 or j == 0:
#                 table[i][j] = 1
#             else:
#                 table[i][j] = table[i][j-1] + table[i-1][j]
#     after_k = table[-1][-1]
#     print(before_k*after_k)


# input = sys.stdin.readline
# n, m, k = map(int, input().split())
# dp = [[0] * (m + 1) for i in range(n + 1)]
# dp[0][1], cnt = 1, 1
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if cnt == k:
#             px = i
#             py = j
#         cnt += 1
#         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
# if k == 0:
#     print(dp[n][m])
# else:
#     print(dp[px][py] * dp[n - px + 1][m - py + 1])


N, M, K = map(int, input().strip().split())

if K == 0:
    table = [[0 for _ in range(M+1)] for __ in range(N+1)]
    table[0][1] = 1

    for i in range(1, N+1):
        for j in range(1, M+1):
            table[i][j] = table[i][j-1] + table[i-1][j]
    print(table[-1][-1])
else:
    k_row = K//M
    k_col = K % M

# 테이블 2개 만들꺼임
    table = [[0 for _ in range(k_col+1)] for __ in range(k_row+2)]
    table[0][1] = 1
    for i in range(1, k_row+2):
        for j in range(1, k_col+1):
            table[i][j] = table[i][j-1] + table[i-1][j]
    before_k = table[-1][-1]

    table = [[0 for _ in range(k_col, M+2)] for __ in range(k_row, N+1)]
    table[0][1] = 1
    for i in range(1, N-k_row+1):
        for j in range(1, M-k_col+2):
            table[i][j] = table[i][j-1] + table[i-1][j]
    after_k = table[-1][-1]

    print(before_k*after_k)
