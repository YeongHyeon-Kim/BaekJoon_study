import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    password = list(input().lstrip('<>-').strip())

    left = []
    right = []

    for pw in password:
        if pw == '<':
            if left:#커서를 오른쪽으로 옮겼을때 left에 하나라도 존재한다면
                right.append(left.pop())
        elif pw == '>':
            if right:
                left.append(right.pop())
        elif pw == '-':
            if left:
                left.pop()
        else:
            left.append(pw)
    
    left.extend(right[::-1])
    ##+했을때 안했을때
    print(''.join(left))








#시간초과 코드
# T = int(input())

# for _ in range(T):
#     password = list(input().lstrip('<>-').strip())
#     length = len(password)
#     result = []
    
#     cursor = 0
#     for i in range(length):
#         if password[i] == '<':
#             cursor -=1
#             pass
#         elif password[i] == '>':
#             cursor +=1
#             pass
#         elif password[i] == '-' and len(result) !=0:
#             cursor -=1
#             result.pop()
#             pass
#         else:
#             result.insert(cursor,password[i])
#             cursor+=1

#     print(''.join(result))

