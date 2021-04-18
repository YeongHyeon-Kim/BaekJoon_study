import math
case = int(input())
def length(d1, d2):
    answer = math.sqrt(((d1[0]-d2[0])**2+(d1[1]-d2[1])**2))
    return answer


for _ in range(case):
    four=0
    two=0
    
    d1 = list(map(int, input().split()))
    d2 = list(map(int, input().split()))
    d3 = list(map(int, input().split()))
    d4 = list(map(int, input().split()))
    leng=[length(d1, d2),length(d1, d3),length(d1, d4),length(d2, d3),length(d2, d4),length(d3, d4)]
    
    check = list(set(leng))
    check.sort()
    if len(check) != 2:
        print(0)
    else:
        if leng.count(check[0]) == 4 and leng.count(check[1]) == 2:
            print(1)
        else:
            print(0)

            
  
        
        
