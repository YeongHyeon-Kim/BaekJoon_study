import sys
input=sys.stdin.readline
T = int(input())

def topological_sort_stack(building, degree,N):
    stack = []
    after_sort = []

    for i in range(N):
        #진입차수가 0인것은 다 넣어주기
        if degree[i] ==0:
            stack.append(i+1)
    
    while stack:
        node = stack.pop()
        after_sort.append(node)

        for i in range(len(building[node])):
            idx = building[node][i]
            degree[idx-1] -= 1 #진입차수 1 낮춰주기
            if degree[idx-1] ==0:
                stack.append(idx)

    return after_sort

for _ in range(T):
    #입력 받기
    N,K = map(int, input().strip().split())
    cost = list(map(int, input().strip().split()))
    building = {i : [] for i in range(1,N+1)}
    degree = [0 for i in range(N)]
    for i in range(1,K+1):
        be, af = map(int,input().strip().split())
        building[be].append(af)
        degree[af-1]+=1
    K = int(input())
    #위상정렬 시작
    order = topological_sort_stack(building,degree,N)
    result = [0 for i in range(N+1)]
    
    for i in range(N):
        now = order[i]
        result[now] += cost[now-1]
        if now == K:
            print(result[now])
            break
        else:
            for j in building[order[i]]:
                result[j] = max(result[j], result[now])

