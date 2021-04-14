N = int(input())
A = list(map(int,input().split(' ')))
B = list(map(int,input().split(' ')))



#B의 원소에 맞게 sort된 A만들기 ->check
a = A.copy()
b = B.copy()
a.sort(reverse=True)
b.sort()
di = {}

for i in range(N):
    ind = b.index(B[i])
    while(True):
        if ind in di.keys():
            ind +=1
        else:
            break
    di[ind] = i
    

check = [0 for i in range(N)]

for key, value in di.items():
    check[value] = a[key]
    
result = 0
for i in range(N):
    result += check[i]*B[i]
    
print(result)



##그냥 답만 만들기

N = int(input())
A = list(map(int,input().split(' ')))
B = list(map(int,input().split(' ')))


a2 = sorted(A, reverse=True)
b2 = sorted(B)

re = 0
for i in range(N):
    re += a2[i]*b2[i]
print(re)