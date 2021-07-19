import sys
input=sys.stdin.readline
N,S = map(int,input().strip().split())

su = list(map(int,input().strip().split()))

def DFS(now, N,S,boo,now_ind):
    global cnt
    if now_ind == N and boo:
        return
    else:
        for i in range(now_ind,N):
            if not visited[i]:
                boo = True
                visited[i] = True
                now += su[i]
                if now == S:
                    cnt+=1
                DFS(now,N,S,boo,i)
                visited[i] = False
                now -= su[i]

cnt = 0
visited = [False for _ in range(N)]
DFS(0,N,S,False,0)

print(cnt)
