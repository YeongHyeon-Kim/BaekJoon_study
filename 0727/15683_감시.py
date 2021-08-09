# import sys
# from copy import deepcopy
# input=sys.stdin.readline

# N, M = map(int, input())
# jido = [list(map(int, input().strip().split())) for _ in range(N)]

# cam_ind = {}
# for i in range(1,6):
#     cam_ind[i] = []

# wall_ind = []
# for i in range(N):
#     for j in range(M):
#         if jido[i][j] == '0':
#             pass
#         elif jido[i][j] == '6':
#             wall_ind.append([i,j])
#         else:
#             cam_ind[jido[i][j]].append([i,j])
# change = 0
# for i in range(5,0,-1):
#     if cam_ind[i]:
#         for k in range(len(cam_ind[i])): # 그 카메라의 개수만큼
#             start_i, start_j = cam_ind[i][k]

#             if i == 5: #카메라 5번이 있다면
#                 for i in range(4):


#             elif i ==4:

#             elif i ==3:

#             elif i ==2:

#             else:

# import sys
# import math
# from collections import deque
# import copy
# input=sys.stdin.readline
# INF=sys.maxsize

# dy=[-1,1,0,0]
# dx=[0,0,-1,1]
# di = [0,[[0],[1],[2],[3]],[[0,1],[2,3]],[[1,2],[1,3],[0,2],[0,3]],[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],[[0,1,2,3]]]

# MIN=9999999999999999
# def dfs(start,MAP,cctv):
#     global MIN
#     if start==len(cctv):
#         cnt=0
#         for y in range(0,row):
#             for x in range(0,col):
#                 if MAP[y][x]==0:
#                     cnt+=1
#         MIN=min(MIN,cnt)
#         return

#     num,y,x = cctv[start]
#     for dir in di[num]:
#         tmp = copy.deepcopy(MAP)
#         for i in dir:
#             ny,nx=y+dy[i],x+dx[i]
#             while row>ny>=0 and col>nx>=0:
#                 if tmp[ny][nx]==6:
#                     break
#                 elif tmp[ny][nx]==0:
#                     tmp[ny][nx]='#'
#                 ny+=dy[i]
#                 nx+=dx[i]
#         dfs(start+1,tmp,cctv)

# if __name__ == "__main__":
#     row,col=map(int,input().split())
#     MAP=[list(map(int,input().split())) for _ in range(row)]
#     cctv=[]
#     block_cnt=0
#     for y in range(0,row):
#         for x in range(0,col):
#             if MAP[y][x] not in [0,6]:
#                 cctv.append([MAP[y][x],y,x])
#             elif MAP[y][x]==6:
#                 block_cnt+=1
#     dfs(0,MAP,cctv)
#     print(MIN)