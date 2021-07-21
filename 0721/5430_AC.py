import sys
from collections import deque
input=sys.stdin.readline

T = int(input())

def solve(fun,su):
    while fun:
        v = fun.popleft()
        cnt = 0
        flag = 0
        if v =='R': # 다음 R이 나올때까지 계속 cnt++
            while fun:
                next_v = fun.popleft()
                if next_v == 'D':
                    cnt+=1
                elif next_v == 'R': ##D개수보다 남아있는 배열의 개수가 크지만 쌍이되는 R을 만났을때
                    flag = 1
                    for _ in range(cnt): #cnt 개수 즉 D개수 만큼 su 마지막을 없애줌
                        su.pop()
                    cnt = 0
                    break
                if cnt > len(su): ##D개수보다 남아있는 배열의 개수가 적으면
                    print('error')
                    return
            #fun 다썻는데 R 안나왔을때
            if flag == 0: #flag로 쌍이 되는 R을 만났는지 확인
                for _ in range(cnt):
                    su.pop()
                su.reverse()
        else:#D를 만났을때
            if len(su) >0:
                su.popleft()
            else:#D를 만났는데 남아있는 수열이 없을때
                print('error')
                return
    
    result = list(su)
    b = '['
    for i in range(len(result)):
        b+=str(result[i])
        if i !=len(result)-1:
            b+=','
    b+=']'
    print(b)


for _ in range(T):
    fun = deque(list(input().replace('RR','').strip()))
    length = int(input())
    su =list(input().strip().lstrip('[').rstrip(']').split(','))
    if length ==0:
        su = deque()
    else:
        su =deque(su)
    solve(fun,su)


#아무리 봐도 이상한 코드라 인터넷 코드 가져옴
#https://it-garden.tistory.com/288
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    p = input()
    n = int(input())
    de = input().strip()[1:-1].split(',')
    p = p.replace('RR','')

    r = 0
    f,b = 0,0

    for j in p:
        if j=='R':
            r +=1
        elif j == 'D':
            if r%2 ==0:
                f +=1
            else:
                b +=1
    if f+b <= n:
        de = de[f:n-b]

        if r%2 ==1:
            print('['+','.join(de[::-1])+']')
        else:
            print('['+','.join(de)+']')
    else:
        print("error")