N = int(input())

stu = []
check = []
for i in range(N):
    stu.append(list(map(int,(input()))))
    check.append(0)
length = len(stu[0])

count = 1
for i in range(length):
    for j in range(N):
        check[j] = int(str(check[j])+str(stu[j][-1-i]))

    if len(set(check)) != N:
        count+=1
    else:
        break

print(count)
    
