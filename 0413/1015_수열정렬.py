size = int(input())
input_ = list(map(int, input().split(' ')))

compare = input_.copy()
input_.sort()
di = []
for i in range(size):
    di.append([i,input_[i]])

result = []
for i in range(size):
    for j in range(size):
        if di[j][1] == compare[i]:
            result.append(di[j][0])
            di[j][1] = max(input_)+1
            #여기서 break를 하지 않으면 만약 1 2 1이 들어왔을 때 맨 처음 1을 확인했음에도
            # 마지막 1까지 확인해버리기 때문에 순서가 잘못 출력됨
            break
            
           
print(str(result)[1:-1].replace(',',''))

