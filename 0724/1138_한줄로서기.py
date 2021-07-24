import sys
input=sys.stdin.readline
from collections import deque

# def right_rotate(num : int, deq):
#     for _ in range(num):
#         deq.appendleft(deq.pop())
#     return deq

#데이터 받기
N = int(input())
memo = list(map(int, input().strip().split()))

result = [0 for _ in range(N)]

for i in range(N):
    cnt = 0 #앞에 있는 0 의 개수
    for j in range(N):
        if result[j] == 0 and cnt!=memo[i]: ##값을 넣을수는 있지만 앞의 0의 개수가 필요한 사람의 수만큼이 아닐때
            cnt+=1 #0 개수를 늘려주고 넘어간다
        elif result[j] == 0 and cnt == memo[i]: #값을 넣을수도 있고 앞의 0의 개수가 필요한 사람의 수만큼일때
            result[j] = i+1 #그 위치에 index+1 즉 키 큰순서대로의 사람 번호를 넣어줌
            break
        else:
            pass #이미 그 위치에 값이 들어가 있으면 pass

print(*result)

        

