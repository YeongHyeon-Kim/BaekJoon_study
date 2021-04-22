num = list(map(int,input()))



N=0
while(len(num)>0):
    N+=1
    tmp = list(map(int,str(N)))
    for i in range(len(tmp)):
        if len(num) ==0:
            break
        elif num[0] == tmp[i]:
            num.pop(0)
    