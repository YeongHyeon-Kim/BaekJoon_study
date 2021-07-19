import sys
input=sys.stdin.readline

N = int(input())

err_num = int(input())

#0 부터 9까지 리모컨
remote_con = {str(i) for i in range(10)}

if err_num >0:
    #고장난 버튼 삭제
    remote_con -= set(map(str,input().strip().split()))

#현재보고 있는 채널 100
current = 100

min_cnt = abs(current-N) # 현재 보고있는 채널에서 숫자 안누르고 + - 로만 움직였을때의 횟수 

#채널은 현재 50만까지 있지만 채널은 무한대만큼 있고, + - 에서 올수있는 방법 2가지를 비교해야 되니까 최대 100만까지 비교할 것임.

for c in range(1000000):
    for j in range(len(str(c))): #c = 1536 , 고장은 1367이라면
        if str(c)[j] not in remote_con: ## 1은 고장난 버튼이니까 누를 수 없음 현재 채널중 하나라도 누를수 없으면
            break # break 함으로써 앞자리 수를 최대한 맞춰줌 2000대에서 -로 시작할수 있게
    else:    
        # elif len(str(c)) -1 == j: #모든 숫자가 다 사용이 가능하다면/ , 자리수 이상 ex 1000으로 움직일껀데 10000으로 더 올라가지 않게 (100만까지 보니까)
        min_cnt = min(min_cnt, abs(c-N)+len(str(c))) # min(다른곳에서 움직인거, 현재 c까지 와서 움직인거)
print(min_cnt)
