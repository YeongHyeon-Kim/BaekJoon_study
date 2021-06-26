import sys
input = sys.stdin.readline

T = int(input())

n = 10000

# 에라토스테네스의 체 
# def isPrime(n):
#     if(n<2):
#         return False
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#     return True

# sosu = []
# for i in range(n+1):
#     if(isPrime(i)):
#         sosu.append(i)

def prime_list(n):
    check = [True] *n
    m = int(n**0.5)
    for i in range(2, m+1):
        if check[i] == True:
            for j in range(i+i, n, i):
                check[j] = False
    return [i for i in range(2, n) if check[i]== True]

sosu = prime_list(n)


length = len(sosu)
for _ in range(T):
    n = int(input())
    min_idx = max([i for i in range(length) if sosu[i]<= n//2])
    boo = True
    for j in range(min_idx,-1,-1):
        if boo:
            for i in range(min_idx,length):
                if sosu[j]+sosu[i] == n:
                    print(str(sosu[j])+' '+str(sosu[i]))
                    boo = False
        else:
            break



#2003
#1929
