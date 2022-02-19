from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().strip().split()))
M = int(input())
li = list(map(int, input().strip().split()))

for i in li:
    if i in A:
        print(1)
    else:
        print(0)


input = sys.stdin.readline


def sol():
    input()
    a = set(input().split())
    input()
    ans = []
    for i in input().split():
        ans.append('1' if i in a else '0')
    print('\n'.join(ans))


sol()


input = sys.stdin.readline

T = int(input())


def solve(N, M, li, num):
    while(True):
        if M == check[0] and max(li) == li[0]:
            print(num)
            return
        elif max(li) == li[0]:
            num += 1
            li.popleft()
            check.popleft()
        else:
            li.rotate(-1)
            check.rotate(-1)


for i in range(T):
    N, M = map(int, input().strip().split())
    li_ = list(map(int, input().strip().split(' ')))
    li = deque(li_)
    num = 1
    check = deque([i for i in range(N)])
    solve(N, M, li, num)
