import sys
input = sys.stdin.readline

N = int(input())

count = 0
check=1
while(True):
    if N >= 10**check:
        count += (10**(check-1))*9*check
        check +=1
    else:
        minus_ = (N+1)-(10**(check-1))
        count += (minus_*check)
        break

print(count)