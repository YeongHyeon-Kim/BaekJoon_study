A,B = map(list, input().split(' '))

divide = []

for i in range(len(B)-len(A)+1):
    divide.append(B[i:i+len(A)])
    
count = []
for i in range(len(divide)):
    tmp=0
    for j in range(len(A)):
        if A[j] != divide[i][j]:
            tmp+=1
    count.append(tmp)
    
print(min(count))
