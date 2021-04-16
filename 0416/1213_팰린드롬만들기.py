import math

name = list(input())

name.sort(reverse=True)

result = []
remain=[]
boo = True
i=0
if (len(name) %2) == 0:
    while(i<len(name)/2):
        if name[2*i] == name[2*i+1]:
            result.append(name[2*i])
            result.insert(0,name[2*i+1])
            i+=1
        else:
            boo =False
            break
    
else:
    num = math.ceil(len(name)/2)
    while(i<=num):
        if i+1 == num:
            if len(remain) ==0:
                result.insert(len(name)//2,name[-1])
            else:
                result.insert(len(name)//2,remain[0])
            break
        
        elif name[2*i] == name[2*i+1]: #앞뒤가 같을때
            result.append(name[2*i])
            result.insert(0,name[2*i+1])
            i+=1
        else:##마지막이 아닌데 앞뒤가 다를때
            remain.append(name.pop(2*i))
            
            if len(remain)>=2:
                boo = False
                break

if boo:
    print(''.join(result))
else:
    print("I'm Sorry Hansoo")