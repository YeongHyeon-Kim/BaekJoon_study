from collections import deque

N, M = map(int,input().split(' '))
location = list(map(int,input().split(' ')))

q = deque(range(1,N+1))

def left_rotate(q):
    tmp = q.popleft()
    q.append(tmp)

def right_rotate(q):
    tmp = q.pop()
    q.insert(0,tmp)

count = 0
for i in range(len(location)):
    if location[i] == q[0]:
        q.popleft()
    
    else:
        if q.index(location[i]) <= len(q)/2:
            while(True):
                left_rotate(q)
                count+=1
                if location[i] == q[0]:
                    q.popleft()
                    break
        else:
            while(True):
                right_rotate(q)
                count+=1
                if location[i] == q[0]:
                    q.popleft()
                    break
        
print(count)
