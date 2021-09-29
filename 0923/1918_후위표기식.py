import sys
from collections import deque
input = sys.stdin.readline


strn = list(input())
stack = []
res = ''
for s in strn:
    if s.isalpha():  # 알파벳은 나오는대로 넣어줌
        res += s
    else:
        if s == '(':  # 여는 괄호 스택 추가
            stack.append(s)
        elif s == '*' or s == '/':  # 연산순위 높은게 나오면 그 전에 나왔던 우선순위 높았던 것들 추가 / 바로 추가 안하는 이유는 괄호가 있기 때문에
            # 앞에 나왔던 우선순위 높은것들 추가
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(s)  # 지금 나온 연산자는 나중에 다시 뽑아서
        elif s == '+' or s == '-':  # 우선 순위 낮은게 나오면 중위 후위식으로는 )가 나온것과 같음 앞에꺼 다 추가
            while stack and stack[-1] != '(':  # 직전에 괄호가 나온게 아니면 앞에꺼는 연산
                res += stack.pop()
            stack.append(s)
        elif s == ')':  # 닫는 괄호 나오면 안에 있는거 ( 나올때까지 pop해서 추가
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()  # ( 직전까지 뽑았으니 하나더 뽑아야함

while stack:  # 남은거 다 추가
    res += stack.pop()
print(res)


# infix = list(input().strip())

# op = ['+', '-', '/', '*']

# front_bracket = 0
# back_bracket = 0

# num_li = []
# operator_li = deque()

# ans = []

# for i in infix:
#     if i.isalpha():
#         ans.append(i)

#     else:
#         if i == '(':
#             operator_li.append(i)
#         elif i =='*' or i =='/':
#             while operator_li and (operator_li[])


# op = ['+', '-', '/', '*']

# front_bracket = 0
# back_bracket = 0

# num_li = []
# operator_li = deque()

# ans = []
# for i in infix:
#     if i == '(':
#         front_bracket += 1

#     elif i == ')':
#         back_bracket += 1
#         if front_bracket == back_bracket:  # 괄호가 현재까지 모두 닫혔을때
#             ans.extend(num_li)
#             num_li = []
#             while operator_li:
#                 ans.append(operator_li.pop())
#     elif i in op:
#         operator_li.append(i)
#     else:
#         num_li.append(i)

# if num_li:
#     ans.extend(num_li)
#     while operator_li:
#         ans.append(operator_li.pop())

# print(''.join(ans))
