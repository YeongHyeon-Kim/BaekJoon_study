N,M = map(int, input().split())

result = [0]*M
visited = [False]*N

def solve(depth,N,M):
    if depth == M:
        print(str(result)[1:-1].replace(',',''))
        return
    else:
        for i in range(1,N+1):
            if not visited[i-1] and result[depth-1] < i:
                visited[i-1] = True
                result[depth] = i
                solve(depth+1,N,M)
                visited[i-1] = False
                result[depth] = 0
solve(0,N,M)

