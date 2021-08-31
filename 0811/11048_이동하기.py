import sys
input=sys.stdin.readline

N,M = map(int, input().strip().split())

jido = [list(map(int,input().strip().split())) for _ in range(N)]

result = [[0 for _ in range(M)] for __ in range(N)]

result[0][0] = jido[0][0]
##값은 가져오면 더 쉬움

for i in range(N):
    for j in range(M):
        if i ==0:
            if j !=0:
                result[i][j]= result[i][j-1] + jido[i][j]
        elif j==0:
            result[i][j] = result[i-1][j] + jido[i][j]
        else:
            result[i][j] += max(result[i][j-1], result[i-1][j]) + jido[i][j]

print(result[N-1][M-1])
