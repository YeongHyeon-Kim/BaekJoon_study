word = list(input())
find_word = list(input())

i=0
count = 0
while(i<len(word)):
    if word[i:i+len(find_word)] == find_word:
        count+=1
        del word[i:i+len(find_word)]
        
    else:
        i+=1
print(count)