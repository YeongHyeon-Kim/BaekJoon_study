S = int(input())

def FindHanSu(N):
    sum = 99
    for i in range(N+1):
        arr = list(map(int, str(i)))
        if N<100:
            sum = N
        elif 100<=i<1000:
            if (arr[2]-arr[1])==(arr[1]-arr[0]):
                sum = sum+1
            elif arr[2]==arr[1]==arr[0]:
                sum = sum+1
    print(sum)
FindHanSu(S)

