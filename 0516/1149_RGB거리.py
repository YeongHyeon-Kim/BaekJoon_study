import sys
input = sys.stdin.readline

N = int(input())

home = []
for i in range(N):
    home.append(list(map(int,input().strip().split())))


sum = []
sum.append(home[0])

for i in range(1,N):
    tmp = []
    ##2번집 R
    tmp.append(home[i][0]+min(sum[i-1][1],sum[i-1][2]))
    ##2번집 G
    tmp.append(home[i][1]+min(sum[i-1][0],sum[i-1][2]))
    ##2번집 B
    tmp.append(home[i][2]+min(sum[i-1][0],sum[i-1][1]))

    sum.append(tmp)

print(min(sum[-1]))
