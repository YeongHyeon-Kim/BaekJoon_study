# 메모제이션 기법 안쓴것.
# T = int(input())
# def fibonachi(i,count0,count1):
#     if i ==0:
#         count0+=1
#     elif i==1:
#         count1+=1
#     else:
#         count0, count1 = fibonachi(i-1,count0,count1)
#         count0, count1 = fibonachi(i-2,count0,count1)
#     return count0, count1
# for i in range(T):
#     N = int(input())
#     count0, count1 = fibonachi(N,0,0)
#     print(str(count0)+' '+str(count1))


# 메모제이션 기법 사용
T = int(input())

fibo = {0:[1,0],1:[0,1]}
def fibonachi(i):
    if i in fibo:
        return fibo[i]
    else:
        fibo[i] = [(fibonachi(i-1)[0] + fibonachi(i-2)[0]),(fibonachi(i-1)[1] + fibonachi(i-2)[1])]
        return fibo[i]
for i in range(T):
    N = int(input())
    tmp = fibonachi(N)
    print(str(tmp[0])+' '+ str(tmp[1]))