N, score, P = map(int,input().split(' '))

if N == 0:
    print(1)
else:
    rank = list(map(int, input().split(' ')))
    rank.append(score)
    rank.sort(reverse=True)
    ind = rank.index(score)
    if ((P == N) & (score<=rank[-1])):
        print(-1)
    else:
        print(ind+1)

