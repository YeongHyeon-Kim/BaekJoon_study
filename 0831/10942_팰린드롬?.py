# import sys
# input=sys.stdin.readline

# N = int(input())
# num = list(map(int, input().strip().split()))
# num = list(map(chr, num))

# M = int(input())
# for _ in range(M):
#     S, E = map(int, input().split())
    
#     check = ''.join(num[S-1:E])
#     if check == check[::-1]:
#         print(1)
#     else:
#         print(0)

import sys
input=sys.stdin.readline



N = int(input())
num = list(map(int, input().strip().split()))
dp = [[0 for _ in range(N)] for __ in range(N)]
for i in range(N): # for 1
    for start in range(N): # for 2
        end = start + i
        if end >= N: #end가 넘는순간 for 2 나가기
            break
        if start == end: #자기자신 1 예시에서 3 3 =1 이니까
            dp[start][end] = 1
            continue
        if start+1 == end: # 바로뒤와 비교했을때
            if num[start] == num[end]:
                dp[start][end] = 1
                continue
        if num[start] == num[end] and dp[start+1][end-1]: # start부터 end 비교 / 안에 있는 수들이 팰린드롬이고, 양끝이 같으면 팰린드롬
            dp[start][end] = 1

m = int(input())
for _ in range(m):
    S,E = map(int, input().split())
    print(dp[S-1][E-1])