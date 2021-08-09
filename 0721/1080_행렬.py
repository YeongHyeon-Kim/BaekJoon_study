import sys
input=sys.stdin.readline

#--------데이터 받아오기

N,M = map(int, input().strip().split())

A = [[] for i in range(N)]
for i in range(N):
    A[i] = list(map(int, input().strip()))

B = [[] for i in range(N)]
for i in range(N):
    B[i] = list(map(int, input().strip()))

#--------함수 만들기

def change(k,l,graph):
    for i in range(-1,2):
        for j in range(-1,2):
                if graph[k+i][l+j] == 1:
                    graph[k+i][l+j] = 0
                else:
                    graph[k+i][l+j] = 1
    return graph

cnt = 0
def solve(N,M,A,B):
    global cnt
    for i in range(N): #
        for j in range(M):
            if i >= N-2 or j >= M-2: # 3*3으로 바꿀수 없는 부분이 만약 다르다면 불가능하다는 뜻
                if A[i][j] != B[i][j]:
                    print(-1)
                    return
            else:
                if A[i][j] != B[i][j]:
                    A = change(i+1, j+1, A)
                    cnt+=1
    print(cnt)

##N이나 M 둘중 하나가 3보다 작으면 change 불가능
def solve2(N,M,A,B):
    for i in range(N): #
        for j in range(M): 
            if A[i][j] != B[i][j]:
                print(-1)
                return
    print(0)



if N >=3 and M >=3:
    solve(N,M,A,B)
else:
    solve2(N,M,A,B)
