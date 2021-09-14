import heapq
import sys
input=sys.stdin.readline

N = int(input())

heap = []
check = {}
for i in range(N):
    input_ = int(input())
    input_check = abs(input_)
    if input_check not in check:
        check[input_check] = []
    
    if input_== 0 and len(heap) == 0:
        print(0)

    elif input_== 0:
        pop_num = heapq.heappop(heap)
        print(heapq.heappop(check[pop_num]))

    else:
        heapq.heappush(heap, input_check)
        
        heapq.heappush(check[input_check], input_)


### heapq 공부해보기
