import sys
input = sys.stdin.readline

A = int(input())

su = list(map(int,input().strip().split()))
result = [0 for i in range(A)]

for i in range(A):
    for j in range(i):
        if su[i] > su[j] and result[i] < result[j]:
            result[i] = result[j]
    result[i] +=1

print(max(result))




## 디버깅 해보기
def solution(n,arr):
    result = [0 for _ in range(n+1)]
    maxlen = 0

    for n in arr:
        for j in range(maxlen,-1,-1):
            if result[j] < n:
                if j == maxlen:
                    maxlen = maxlen + 1
                    result[maxlen] = n
                else:
                    result[j+1] = min(result[j+1],n)
                break




    return maxlen



def main():
    n = int(input())
    arr = list(map(int,input().split()))
    print(solution(n,arr))

main()