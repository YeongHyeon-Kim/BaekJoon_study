import sys
input = sys.stdin.readline

N = int(input())

paper = []
for i in range(N):
    tmp = list(map(int,input().strip().split()))
    paper.append(tmp)

blue = 0
white = 0
def quadtree(x,y,n):
    global blue, white
    check = paper[x][y]
    for i in range(x,x+n):
        for j in range(y, y+n):
            if check != paper[i][j]:
                quadtree(x,y,n//2)
                quadtree(x,y+n//2,n//2)
                quadtree(x+n//2,y,n//2)
                quadtree(x+n//2,y+n//2,n//2)
                return
    if check == 0:
        white+=1
        return
    else:
        blue+=1
        return

quadtree(0,0,N)
print(white)
print(blue)

