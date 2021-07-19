import sys
input=sys.stdin.readline

k = int(input())
sign = list(input().strip().split())

small_result = [-1 for i in range(k+1)]
big_result = [-1 for i in range(k+1)]


used = [False for i in range(10)]
sign_used = [False for i in range(k)]


used_s = [False for i in range(10)]
sign_used_s = [False for i in range(k)]
def find_small(depth,M):
    global small_result      
    if depth == M+1:
        small_result = list(map(str,small_result))
        print(''.join(small_result))
        exit(0)
    else:
        for i in range(10):
            if not used_s[i]:
                if depth==0:
                    small_result[depth] = i
                    used_s[i] = True
                    find_small(depth+1, M)
                    small_result[depth] = -1
                    used_s[i] = False
                elif sign[depth-1] == '<' and not sign_used_s[depth-1]:
                    sign_used_s[depth-1] = True
                    if small_result[depth-1]<i:
                        used_s[i] = True
                        small_result[depth] = i
                        find_small(depth+1, M)
                        used_s[i] = False
                        small_result[depth] = -1
                elif not sign_used_s[depth-1]:
                    sign_used_s[depth-1] = True
                    if small_result[depth-1]>i:
                        used_s[i] = True
                        small_result[depth] = i
                        find_small(depth+1, M)
                        used_s[i] = False
                        small_result[depth] = -1
                sign_used_s[depth-1] = False

def find_big(depth,M):
    global big_result        
    if depth == M+1:
        big_result = list(map(str,big_result))
        print(''.join(big_result))
        find_small(0,k)
        exit(0)
    else:
        for i in range(9,-1,-1):
            if not used[i]:
                if depth==0:
                    big_result[depth] = i
                    used[i] = True
                    find_big(depth+1, M)
                    big_result[depth] = -1
                    used[i] = False
                elif sign[depth-1] == '<' and not sign_used[depth-1]:
                    sign_used[depth-1] = True
                    if big_result[depth-1]<i:
                        used[i] = True
                        big_result[depth] = i
                        find_big(depth+1, M)
                        used[i] = False
                        big_result[depth] = -1
                elif not sign_used[depth-1]:
                    sign_used[depth-1] = True
                    if big_result[depth-1]>i:
                        used[i] = True
                        big_result[depth] = i
                        find_big(depth+1, M)
                        used[i] = False
                        big_result[depth] = -1
                sign_used[depth-1] = False


find_big(0,k)