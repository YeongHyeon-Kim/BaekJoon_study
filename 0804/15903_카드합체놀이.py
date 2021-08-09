import sys
input=sys.stdin.readline

N,M = map(int, input().strip().split())
card = list(map(int, input().strip().split()))
card.sort()

for _ in range(M):
    tmp = card[0]+card[1]
    card[0] = tmp
    card[1] = tmp
    card.sort()

print(sum(card))