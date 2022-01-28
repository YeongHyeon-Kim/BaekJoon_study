import sys
N, M = map(int, sys.stdin.readline().split())
chess = []
result = []
Blist = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
Wlist = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
Bstart = []
Wstart = []
for i in range(4):
    Bstart.append(Blist)
    Bstart.append(Wlist)
for i in range(4):
    Wstart.append(Wlist)
    Wstart.append(Blist)

for i in range(N):  # chess 만들기
    chess_col = list(sys.stdin.readline().strip())
    if len(chess_col) == M:
        chess.append(chess_col)

for c_r in range(N-7):
    for c_c in range(M-7):
        wcnt = 0
        bcnt = 0
        for i in range(8):
            for j in range(8):
                if chess[c_r+i][c_c+j] == Wstart[i][j]:
                    pass
                else:
                    wcnt += 1
                if chess[c_r+i][c_c+j] == Bstart[i][j]:
                    pass
                else:
                    bcnt += 1
        result.append(wcnt)
        result.append(bcnt)
print(min(result))
