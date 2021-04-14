'''
틀림 / 0414에 다시 해결 / 해결 완료
'''
# N, M = map(int,input().split(' '))
# location = list(map(int,input().split(' ')))
# present = N

# final_count = 0
# count = 0
# boo = True
# for i in range(len(location)):
#     k = location[i]
#     j = i 
#     if k <= (present/2):
        
#         while(k>1):
#             k -= 1
#             count +=1
            
#         present -=1
        
#         while(j+1<len(location)):
#             if count ==0:
#                 location[j+1] -=1
#             location[j+1] -=count
#             if location[j+1] == 0:
#                 location[j+1] = present  
#             j+=1
#     else:
#         while(k>1):
#             if k == present:
#                 k = 1
#                 count+=1
#             else:
#                 k += 1
#                 count +=1  
#         present -=1
        
#         while(j+1<len(location)):
#             location[j+1] +=count
#             if location[j+1] == present:
#                 location[j+1] = 1
#             elif location[j+1] > present:
#                 tmp = location[j+1] - present
#                 location[j+1] = tmp   
#             j+=1
#     j = i   
#     while(j+1<len(location)):
#         location[j+1] -=1
#         if location[j+1] == 0:
#             location[j+1] = present  
#         j+=1
    
#     final_count += count
#     count=0
    
# location -1
