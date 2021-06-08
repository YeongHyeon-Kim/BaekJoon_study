import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split(' '))

height = list(map(int, input().strip().split(' ')))

##이진트리라 맥스도 굳이 잡을필요 없음
max_height = max(height)

def count(height, mid):
    ##목표하는 값보다 커지면 더하기 바로 빠져나오기
    total=sum([i-mid if mid < i else 0 for i in height])
    return total

def find(max_height, min_height, height, M):
    while(min_height<max_height+1):
        mid = int((max_height+min_height)/2)
        now = count(height,mid)
        if M == now:
            print(mid)
            return
        elif M < now:
            min_height = mid
        else:
            max_height = mid
    print(min_height)
    return

find(max_height,0,height,M)

