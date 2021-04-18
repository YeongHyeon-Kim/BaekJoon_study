
from collections import deque

N = int(input())
move = list(input())

#시작이 N이니까
direction = deque(['S','W','N','E'])

x=0
y=0

entire = set()
entire.add((x,y))

x_lot = set()
x_lot.add(x)
y_lot = set()
y_lot.add(y)


for i in range(N):
    if move[i] == 'R':
        direction.rotate(-1)
    
    elif move[i] == 'L':
        direction.rotate(1)
        
    else:
        if direction[0] == 'E':
            x+=1
        elif direction[0] == 'W':
            x-=1
        elif direction[0] == 'N':
            y+=1
        else:
            y-=1
    
    entire.add((x,y))
    x_lot.add(x)
    y_lot.add(y)

x_len = len(x_lot)
y_len = len(y_lot)

xMin = -min(x_lot)
yMin = -min(y_lot)

jido = []
for i in range(y_len):
    tmp = []
    for j in range(x_len):
        tmp.append('#')
    jido.append(tmp)
    


for y in range(y_len):
    for x in range(x_len):
        if (x-xMin,y-yMin) in entire:
            jido[y][x] = '.'


for i in range(y_len-1,-1,-1):
   
    print(''.join(jido[i]))




