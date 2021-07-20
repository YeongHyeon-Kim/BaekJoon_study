# import sys
# input=sys.stdin.readline

# N,M = map(int, input().strip().split())

# computer = {}
# #데이터 받아오기
# for i in range(M):
#     A, B = map(int, input().strip().split())
#     #A가 B를 신뢰한다 -> B를 해킹하면 A는 해킹할수 있다.
#     if B not in computer:
#         computer[B] = [A]
#     else:
#         computer[B].append(A)

# result = {i: 1 for i in range(N+1)}
# visited = [False for i in range(N+1)]


# def DFS(start):
#     if visited[start] == True:
#             pass
#     else:
#         if start in computer:
#             for child in computer[start]:
#                 DFS(child)
#                 visited[child] = True
#                 result[start] += result[child]
#         else:
#             visited[start] = True

# for i in range(1,N+1):
#     DFS(i)

# max_ = max(result.values())
# final = [k for k,v in result.items() if v == max_]

# print(*final)



##DFS는 불가능한 문제인가?.,..



import sys
from collections import deque
input=sys.stdin.readline


N,M = map(int, input().split())
computer = [[] for _ in range(N+1)]
#데이터 받아오기
for i in range(M):
    A, B = map(int, input().split())
    #A가 B를 신뢰한다 -> B를 해킹하면 A는 해킹할수 있다.
    computer[B].append(A)


def BFS(start):
    cnt = 0
    q = deque()
    q.append(start)
    visited = [False for i in range(N+1)]
    visited[start] = True
    while q:
        now = q.popleft()
        cnt+=1 ##자기자신 해킹하면 +1
        for child in computer[now]:
            ##start에 연결되어있는 child가 있으면
            if not visited[child]:
                visited[child] = True
                q.append(child)
    return cnt

max_ = 0
result = []
for i in range(1, N+1):
    if computer[i]: ##i로 시작하는게 있으면 /  비어있지 않으면
        tmp = BFS(i) #일단 값을 저장
        if max_ <= tmp: #tmp가 max_값보다 크면 원래 가지고 있던 result 초기화 및, max 
            if max_ < tmp:
                result = []
            max_ = tmp
            result.append(i) ## tmp가 max_보다 크면 초기환된 result에 값이 append 되고 같으면 앞에 있던거에 그대로 append
print(*result)

