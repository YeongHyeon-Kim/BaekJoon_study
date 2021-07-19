import sys
input=sys.stdin.readline

def isprime(n : int):
    sosu = [True for i in range((2*n)+1)]
    sosu[1] = False
    ra_n = int((2*n)**0.5)
    for i in range(1,ra_n+1):
        if sosu[i]:
            ##길이를 2n 까지 했으니까 바꾸는 범위도 2*n+1 로 해야지 2*n까지 바꿈 
            for j in range(i+i,2*n+1,i):
                sosu[j] = False
    return sosu

sosu = isprime(123456)
#최대 길이까지 만들어두기

while(1):
    n = int(input())
    if n==0:
        break
    cnt= 0
    for i in range(n+1,2*n+1):
        if sosu[i]:
            cnt+=1
    print(cnt)

#시간초 차이가 어디서 나는지???



#인터넷 코드
N = 123456 * 2 + 1
sieve = [True] * N
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N, i):
            sieve[j] = False

def prime_cnt(val):
    cnt = 0
    for i in range(val + 1, val * 2 + 1):
        if sieve[i]:
            cnt += 1
    print(cnt)

while True:
    val = int(input())
    if val == 0:
        break
    prime_cnt(val)