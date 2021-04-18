#해결 못함..

First, End = map(int, input().split(' '))
X,y = map(int, input().split(' '))


i=First

while(i<=End):
    if i%X == y:
        if (i+X) <= End:
            print('Unknwon Number')
            break
        else:
            print(i)
            break
    else:
        if y-(First%X) > 0:
            i += y-(First%X)
        else:
            i += y-(First%X)
            i += X
            
if i>End:
     print('Unknwon Number')           
            

