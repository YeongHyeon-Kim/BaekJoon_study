import sys
input=sys.stdin.readline

M,N,K = map(int, input().strip().split())
jido = [[False for _ in range(N)] for __ in range(M)]

for _ in range(K):
    lx,ly,rx,ry = map(int, input().strip().split())
    for j in range(ly,ry):
        for k in range(lx,rx):
            jido[j][k] = True

cnt = 0
area = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for i in range(M):
    for j in range(N):
        if not jido[i][j]:
            tmp_area = 1
            cnt+=1
            tmp = [[i,j]]
            jido[i][j] = True
            while tmp:
                i_,j_ = tmp[0][0], tmp[0][1]
                del tmp[0]
                for k in range(4):
                    new_i = i_ + dx[k]
                    new_j = j_ + dy[k]
                    if 0<=new_i<M and 0<=new_j<N and not jido[new_i][new_j]:
                        tmp_area+=1
                        tmp.append([new_i,new_j])
                        jido[new_i][new_j] = True
            area.append(tmp_area)
print(cnt)
print(*sorted(area))