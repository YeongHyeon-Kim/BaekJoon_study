import sys
input=sys.stdin.readline

n, m = map(int, input().strip().split())

fac = [1 for i in range(n+1)]
for i in range(1,n+1):
    fac[i] = fac[i-1]*i

print((fac[n]//(fac[n-m]*fac[m])))

# print(int(fac[n]/(fac[n-m]*fac[m])))
#/를 하고 나중에 int로 바꾸면 나누는 순간 실수오차가 발생하므로 뒤늦게 int로 바꾸어도 늦습니다. 대신에 //를 쓰면 됩니다