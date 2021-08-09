import heapq
import sys
input=sys.stdin.readline

N = int(input())

heap = []
for i in range(N):
    input_ = int(input())
    if input_== 0 and len(heap) == 0:
        print(0)
    elif input_== 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, input_)