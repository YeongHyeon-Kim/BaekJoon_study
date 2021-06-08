N = int(input())
time = list(map(int, input().split(' ')))
time.sort()

sum_ = [time[0]]
for i in range(1,N):
    sum_.append(sum_[i-1] + time[i])

print(sum(sum_))

## 1 2 3 4 5 
##   2 3 4 5  이런식으로 1*1 2*2 3*3번 이런식으로도 구할수있음