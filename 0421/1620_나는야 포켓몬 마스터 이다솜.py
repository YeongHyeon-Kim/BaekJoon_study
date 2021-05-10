import sys

N, M = map(int, sys.stdin.readline().rstrip().split())


pocket = {}
for i in range(1,N+1):
    input_ = sys.stdin.readline().rstrip()
    pocket[str(i)] = input_
    pocket[input_] = i

for i in range(M):
    print(pocket[sys.stdin.readline().rstrip()])
        