N = int(input())

dic = {1:1, 2:3, 3:5}

def find(dic, N):
    if N in dic:
        return dic[N]
    else:
        dic[N] = find(dic,N-1) + (find(dic,N-2)*2)
        return dic[N]

print(find(dic,N)%10007)