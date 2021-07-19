import sys
input=sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    #  sti에 바로 값을 변경 시킴으로써 result를 사용하지 않아도 됨
    #  result = [[0 for i in range(n)] in range(2)]
    sti=[]
    for i in range(2):
        sti.append(list(map(int, input().strip().split(' '))))
    ##값 받아오기 완료
    sti[0][1] += sti[1][0]
    sti[1][1] += sti[0][0]

    for i in range(2,n):
        sti[0][i] += max(sti[1][i-1],sti[1][i-2])
        sti[1][i] += max(sti[0][i-1],sti[0][i-2])
    
    print(max(sti[0][-1],sti[1][-1]))

    ##미리 만들고 index 찾아서가 더 빠름