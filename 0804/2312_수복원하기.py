T = int(input())

for _ in range(T):
    N = int(input())

    result ={}
    i = 2
    while True:
        if N == 1:
            break
        else:
            if N % i == 0:
                if i not in result:
                    result[i] = 1
                else:
                    result[i]+=1
                N //=i
            else:
                i+=1
    for k,v in result.items():
        print(str(k)+' '+str(v))
