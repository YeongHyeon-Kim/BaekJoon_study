import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


n = int(input())
lines = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().strip().split())
    lines[a].append(b)
    lines[b].append(a)
dp = [[0, 0] for _ in range(n+1)]
visited = [False for _ in range(n+1)]


def dfs(r):
    visited[r] = 1
    dp[r][0] = 1  # 0은 부모노드(자기자신이 얼리어답터일때)
    for i in lines[r]:
        if not visited[i]:
            dfs(i)
            # 자기자신이 얼리어답터이면 자식이 얼리어답터이든 아니든 상관없음 가장 최소
            dp[r][0] += min(dp[i][0], dp[i][1])
            dp[r][1] += dp[i][0]  # 자기자신이 얼리어답터가 아니라면 자식이 얼리어답터여야함


dfs(1)
print(min(dp[1][0], dp[1][1]))
