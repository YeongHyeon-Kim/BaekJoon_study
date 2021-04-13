"""
1002 터렛 문제

"""
import math

print_value = []
case_num = int(input())
for i in range(case_num):
    x1,y1,r1,x2,y2,r2 = (map(int, input().split(' ')))
   
    
    #원의 중심 사이의 거리
    X = (math.sqrt(((x1-x2)**2)+(y1-y2)**2))
    tmp = 0
    if r1 > r2:
        tmp = r1
        r1 = r2
        r2 = tmp
    
    #원의 중심이 같을때
    if ((x1 == x2) & (y1 == y2)):
        #반지름이 같으면 같은 원 2개 즉 무한대
        if r1 == r2:
            print(-1)
            
        #반지름이 다르면 서로 닿지 않음    
        else:
            print(0)
            
            
    #외접 / 원의 중심 사이의 거리가 두 원 반지름의 합과 같을때 닿는 점 1개        
    elif X == (r1+r2):
        print(1)
        
    #원의 중심 사이의 거리가 두 원 반지름의 합보다 클때 닿는점 0개
    elif X > (r1+r2):
        print(0)
         
    #내접    
    elif ((X+r1) == r2):
        print(1)
        
    #원 안에 원이 있지만 작은 원이 접하지 않을때
    elif ((X+r1) < r2):
        print(0)
        
    #원의 중심 사이의 거리가 두 원 반지름의 합보다 작을때 닿는 점 2개
    elif X < (r1+r2):
        print(2)
        
'''
2개의 점이 생기는 경우가 내접, 원 안에 원이 있지만 작은 원이 접하지 않을때 보다 위의 elif에 있으면
모두 2개의 점으로 판단되기 때문에 맨 마지막에 확인해야함.
'''