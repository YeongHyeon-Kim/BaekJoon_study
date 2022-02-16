import sys
input = sys.stdin.readline
N = int(input())
M = []
for i in range(N):
    M.append(int(input().strip()))

check = [i for i in range(1,N+1)]

stack = []
result = []
def find():
    i = 1
    stack.append(i)
    result.append('+')
    while(len(M) != 0):
        if i < N:
            if stack[-1] == M[0]:
                while(True):
                    if len(stack) != 0 and stack[-1] == M[0]:
                        stack.pop(-1)
                        result.append('-')
                        M.pop(0)
                    else:
                        break
                if i < N+1:
                    i+=1
                    stack.append(i)
                    result.append('+')
            else:    
                i+=1
                stack.append(i)
                result.append('+')
        else:
            if stack[-1] == M[0]:
                stack.pop(-1)
                result.append('-')
                M.pop(0)
            else:
                print("NO")
                return
    for i in range(len(result)):
        print(result[i])

find()