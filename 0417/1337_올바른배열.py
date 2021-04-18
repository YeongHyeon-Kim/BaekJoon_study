N = int(input())

num = []
for i in range(N):
    num.append(int(input()))
num.sort()
i=0
count = []
for i in range(N):
    compare = set(range(num[i],num[i]+5))
    count.append(len(compare.difference(set(num[i:i+5]))))

print(min(count))