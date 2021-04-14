N,M = map(int,input().split(' '))

brand_6 = []
brand_1 = []
for i in range(M):
    tmp1, tmp2 = map(int,input().split(' '))
    brand_6.append(tmp1)
    brand_1.append(tmp2)
    
min_6 = min(brand_6)
min_1 = min(brand_1)

count = 0
money = 0
while(count<N):
    if min_6 < (min_1*6):
        if min_6 < (min_1*(N-count)):
            money += min_6
            count+=6
        else:
            money += min_1*(N-count)
            break
            
    else:
        money = min_1*N
        break
print(money)