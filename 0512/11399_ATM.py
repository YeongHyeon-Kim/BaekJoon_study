N = int(input())
time = list(map(int, input().split(' ')))
time.sort()

sum_ = [time[0]]
for i in range(1,N):
    sum_.append(sum_[i-1] + time[i])

print(sum(sum_))