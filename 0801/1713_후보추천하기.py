import sys
input=sys.stdin.readline

N = int(input())
num = int(input())
chu = list(map(int, input().strip().split()))


chu_num = {}

for i in range(num):
    chuchu = chu[i]
    if len(chu_num) < N:
        if chuchu not in chu_num:
            chu_num[chuchu] = 1
        else:
            chu_num[chuchu] +=1
    else:
        if chuchu not in chu_num:
            
            for j in range(-2,-N-1,-1): #없앨꺼 결정하기
                if chu_num[list(chu_num.keys())[j+1]] != chu_num[list(chu_num.keys())[j]]:
                    chu_num.pop(list(chu_num.keys())[j+1])
                    #del 로 지울것
                    chu_num[chuchu] = 1
                    break
            
            else:# 다 똑같으면 맨 앞에꺼 제거
                chu_num.pop(list(chu_num.keys())[0])
                chu_num[chuchu] = 1
        else:
            chu_num[chuchu] += 1
    chu_num = dict(sorted(chu_num.items(), key= lambda x : x[1], reverse=True))
print(*sorted(chu_num.keys()))

