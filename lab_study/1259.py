import sys
input = sys.stdin.readline

while True:
    n = input().strip()
    length = len(n)
    if n == "0":
        break
    for i in range(1, length//2+1):
        if(n[i-1] != n[-i]):
            print("no")
            break
    else:
        print("yes")


while True:
    n = input().rstrip()
    if n == 0:
        break
    print("yes" if n == n[::-1] else "no")
