N = int(input())

book= []
for i in range(N):
    book.append(input())


uni = list(set(book))
uni.sort()
count = {}

for i in range(len(uni)):
    for j in range(N):
        if book[j] == uni[i]:
            if uni[i] in count:
                count[uni[i]] += 1
            else:
                count[uni[i]] = 1
            

tmp = 0 
result = 'a'

for key, value in zip(count.keys(),count.values()):
    tmp_ = value
    if tmp_ > tmp:
        tmp = tmp_
        result = key


print(result)