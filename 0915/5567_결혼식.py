import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

friend_list = {}

for i in range(m):
    a, b = map(int, input().strip().split())
    if a not in friend_list:
        friend_list[a] = [b]
        if b not in friend_list:
            friend_list[b] = [a]
        else:
            friend_list[b].append(a)
    else:
        friend_list[a].append(b)
        if b not in friend_list:
            friend_list[b] = [a]
        else:
            friend_list[b].append(a)

visited = [False]*(n+1)
visited[0] = True
visited[1] = True
count = 0

if 1 not in friend_list:
    print(0)
else:
    for i in friend_list[1]:
        if not visited[i]:
            count += 1
            visited[i] = True
        for j in friend_list[i]:
            if not visited[j]:
                count += 1
                visited[j] = True
    print(count)
