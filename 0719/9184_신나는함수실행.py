import sys
input=sys.stdin.readline

memo = {'111' : 2, '222' : 4}

def fun_recur(a,b,c):
    if f'{a}{b}{c}' in memo:
        return memo[f'{a}{b}{c}']
    else:
        if a <= 0 or b <= 0 or c<=0:
            memo[f'{a}{b}{c}'] = 1
            return 1
            
        elif a >20 or b >20 or c>20:
            memo[f'{a}{b}{c}'] = fun_recur(20,20,20)
        elif a<b<c:
            memo[f'{a}{b}{c}']= fun_recur(a,b,c-1) + fun_recur(a,b-1,c-1) - fun_recur(a,b-1,c)
        else:
            memo[f'{a}{b}{c}'] = fun_recur(a-1,b,c) + fun_recur(a-1,b-1,c) + fun_recur(a-1,b,c-1) - fun_recur(a-1,b-1,c-1)
        
        return memo[f'{a}{b}{c}']

while 1:
    a,b,c= map(int,input().strip().split())
    if a== -1 and b==-1 and c==-1 :
        break
    else:
        ##결과 출력
        # result = 'w'+'('+f'{a}'+', ' + f'{b}' + ', ' + f'{c}' +')' +' = '+ str(fun_recur(a,b,c))
        print("w(%d, %d, %d) = %d"%(a, b, c, fun_recur(a, b, c)))
        # print(result)

