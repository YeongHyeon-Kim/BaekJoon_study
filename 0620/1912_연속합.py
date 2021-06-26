import sys
input = sys.stdin.readline

n = int(input())
su = list(map(int, input().strip().split()))

result  = [0]*n
result[0] = su[0]

##저장을 할필요가 없음 다시 확인 해보기
#su 를 바꾸면 됨 result 필요 x

for i in range(1,n):
    #result에 도달하기 까지의 최대값을 계속해서 저장하기
    result[i] = max(su[i-1] + su[i], result[i-1] + su[i], su[i])

print(max(result))





