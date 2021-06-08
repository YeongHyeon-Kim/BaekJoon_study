T = int(input())

memo = {0:0,1:1,2:2,3:4}

def count(N):
    if N in memo:
        return memo[N]
    else:
        memo[N] = count(N-1) + count(N-2) + count(N-3)
        return memo[N]

for _ in range(T):
    N = int(input())
    print(count(N))

#재귀보다는 for문으로 하는게 더 낫다.
#재귀는 depth가 1000이상이면 오류가 난다.

#재귀 사용하지 않은 버젼
T = int(input())
memo = [0]*12

def count():
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4
    for i in range(4,12):
        memo[i] = memo[i-1]+memo[i-2]+memo[i-3]
count()

for _ in range(T):
    N = int(input())
    print(memo[N])


