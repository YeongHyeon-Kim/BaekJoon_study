import sys
input=sys.stdin.readline

N = int(input())
su = list(map(int, input().strip().split()))

ca = list(map(int, input().strip().split()))
for i in range(len(ca)):
    if ca[i] > N:
        ca[i] = N-1

calc = ['+' for _ in range(ca[0])] 
calc.extend(['-' for _ in range(ca[1])])
calc.extend(['*' for _ in range(ca[2])])
calc.extend(['/' for _ in range(ca[3])])


visited = [False for _ in range(len(calc))]

max_ = -9999999999999999999999
min_ = 9999999999999999999999
re = su[0]
def DFS(depth, length, now : int):
    global max_
    global min_
    if depth == N:
        max_ = max(max_, now)
        min_ = min(min_, now)
        return
    else:
        for i in range(1,length+1):
            if not visited[i-1]:
                nex =0
                visited[i-1] = True
                chec = calc[i-1]
                if chec == '+':
                    nex = now+ su[depth]
                elif chec == '-':
                    nex = now-su[depth]
                elif chec == '*':
                    nex = now * su[depth]
                else:
                    nex = abs(now)//su[depth]
                DFS(depth+1, length, nex)
                visited[i-1] = False

DFS(1,len(calc), re)
print(max_)
print(min_)


