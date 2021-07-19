import sys
input=sys.stdin.readline

input_ = list(input().strip())

sign = []
num_li = []
num = ""
minus_index = []
j=0
for i in range(len(input_)):
    if input_[i] == '+':
        j+=1
        sign.append(input_[i])
        if num != '':
            num_li.append(int(num))
            num=''
    elif input_[i]=='-':
        minus_index.append(j)
        j+=1
        sign.append(input_[i])
        if num != '':
            num_li.append(int(num))
            num=''
    else:
        num+=input_[i]
        if i==len(input_)-1:
            num_li.append(int(num))



if len(sign) != 0:
    length = len(sign)
    used = [False for i in range(length+1)]
    result = []
    tmp = 0
    for i in range(len(minus_index)-1,-1,-1):
        for j in range(minus_index[i],length):
            tmp += num_li[j+1]
            used[j+1] = True
        result.append(-tmp)
        tmp = 0
        length -= length-minus_index[i]
    
    for i in range(length+1):
        if not used[i]:
            result.append(num_li[i])
    print(sum(result))
else:
    print(num_li[0])

##1등 코드
# e = [sum(map(int, x.split('+'))) for x in input().split('-')]
# print(e[0]-sum(e[1:]))