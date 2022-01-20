import sys
input = sys.stdin.readline

# DP 문제풀이
N = int(input())
re = [5001] * (N+5)
re[3] = 1
re[5] = 1
for i in range(6, N+1):
    re[i] = min(re[i-3]+1, re[i-5]+1)

if re[N] >= 5000:
    print(-1)
else:
    print(re[N])


# 인터넷 정석 문제풀이
N = int(input())
result = 0

while N >= 0:
    if N % 5 == 0:
        result += (N//5)
        print(result)
        break
    N -= 3
    result += 1
else:
    print(-1)
