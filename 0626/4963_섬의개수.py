import sys
input=sys.stdin.readline

def BFS(x : int,y : int):
        queue=[[y,x]]

        while queue:
            y,x = queue[0][0], queue[0][1]
            del queue[0]

            dx = [1,-1,0,0,-1,-1,1,1]
            dy = [0,0,-1,1,-1,1,-1,1]

            for i in range(8):
                b = y +dy[i]
                a = x +dx[i]

                if 0<=b<h and 0<=a<w and graph[b][a] == 1:
                    graph[b][a] =0
                    queue.append([b,a])


while(1):
    w,h = map(int, input().strip().split())
    if w==0 and h ==0:
        break
    else:
        graph =[]
        for _ in range(h):
            graph.append(list(map(int,input().strip().split())))
        
        cnt = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j] ==1:
                    graph[i][j] = 0
                    BFS(j,i)
                    cnt+=1
    print(cnt)
