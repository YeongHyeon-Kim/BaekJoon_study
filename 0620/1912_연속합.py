import sys
input = sys.stdin.readline

n = int(input())
su = list(map(int, input().strip().split()))

result  = [0]*n
result[0] = su[0]

for i in range(1,n):
    #result에 도달하기 까지의 최대값을 계속해서 저장하기
    result[i] = max(su[i-1] + su[i], result[i-1] + su[i], su[i])

print(max(result))





