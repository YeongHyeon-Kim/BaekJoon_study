import sys
input=sys.stdin.readline

def DFS(depth : int, N : int, M : int):
    if depth ==M:
        print(*result)
    else:
        for i in range(N):
            if not visited[i] and result[depth-1] < s[i]:
                result[depth] = s[i]
                visited[i] = True
                DFS(depth+1, N,M)
                visited[i] = False
                result[depth] =0 
i=0
while(1):
    input_ = list(map(int, input().strip().split()))
    k = input_[0]
    if k==0:
        break
    else:
        if i !=0:
            print()
        s = input_[1:]
        N = len(s)
        visited = [False for i in range(N)]
        result = [0 for i in range(6)]
        DFS(0,N,6)
        i+=1
    
    