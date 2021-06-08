import sys
input = sys.stdin.readline
def find_budget(M,request):
    min_ = 0
    max_ = request[-1]
    
    while(min_<=max_):
        mid_ = int((min_+max_)/2)
        check = 0
        for i in range(N):
            if request[i]<mid_:
                check+= request[i]
            else:
                check+=mid_
        if check == M:
            return mid_
        elif M > check:
            min_ = mid_+1
        else:
            max_ = mid_-1
    return max_

N = int(input())

request = list(map(int,input().strip().split()))
request.sort()
M = int(input())
sum_request = sum(request)
if M < sum_request:
    result = find_budget(M,request)
    print(result)
else:
    print(request[-1])


