N = int(input())

zoo = [[0 for _ in range(3)] for __ in range(N+1)]
for i in range(3):
    zoo[1][i] = 1
for i in range(2,N+1):
    zoo[i][0] = (zoo[i-1][1] + zoo[i-1][2])%9901
    zoo[i][1] = (zoo[i-1][0] + zoo[i-1][2])%9901
    zoo[i][2] = (zoo[i-1][0] + zoo[i-1][1] + zoo[i-1][2])%9901

print(sum(zoo[N])%9901)