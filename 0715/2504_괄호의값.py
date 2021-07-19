import sys
input=sys.stdin.readline

input_= list(input().strip())

stack = []
def cal(input_):
    for i in input_:#한개씩 빼온다
        if i ==')':
            value = 0
            while stack:
                before = stack.pop()
                if before == '(':
                    if value ==0: ##before 맨 처음이 ( 값이여서 바로 () 인경우 숫자 2
                        stack.append(2)
                    else:
                        stack.append(2*value) ##before 중에 (X) 이러한 경우가 있는 것
                    break ## i 의 짝 ( 를 찾았기 때문에 더이상 비교 안함
                elif before == '[':
                    print(0) ## )과 맞지 않는 짝 [ 가 들어옴
                    return
                else:
                    value += before ## 앞에 숫자가 있어서 XY 인 경우를 나타냄 --> 언젠가는 ( 를 만나서 어떠한 결과가 append 된다.
        
        elif i ==']':
            value = 0
            while stack:
                before = stack.pop()
                if before == '[':
                    if value ==0: ##before 맨 처음이 [ 값이여서 바로 [] 인경우 숫자 3
                        stack.append(3)
                    else:
                        stack.append(3*value) ##before 중에 [X] 이러한 경우가 있는 것
                    break ## i 의 짝 [ 를 찾았기 때문에 더이상 비교 안함
                elif before == '(':
                    print(0) ## ]과 맞지 않는 짝 ( 가 들어옴
                    return
                else:
                    value += before ## 앞에 숫자가 있어서 XY 인 경우를 나타냄 --> 언젠가는 ( 를 만나서 어떠한 결과가 append 된다.
        else:
            stack.append(i) ##괄호가 닫힐때까지 계속 집어넣기
    
    final_result = 0
    for i in stack:
        if i =='(' or i=='[':##닫힌거를 다찾아서 매칭 시켰는데도 남아있을때 잘못된 경우
            print(0)
            return
        else:
            final_result+=i
    #print(0)없이 잘 끝났다면
    print(final_result)
    return
cal(input_)