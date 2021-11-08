N = int(input())
board = [-100 for _ in range(N)]  # 의미 없는 수로 채우기, 각 행에 어떤 열에 퀸이 놓일지 저장하는 것


def isOkay(idx: int):
    for i in range(idx):  # 위에 것과만 비교하면 되기 때문에 idx로
        # 여태껏 정해졌던 값들 중에 하나라도 같은 열 체크, 대각선 체크
        if ((board[i] == board[idx]) or ((idx-i) == abs(board[idx]-board[i]))):
            return 0

    return 1  # 위에 모두 해당하지 않는다면 놓을 수 있는 자리


count = 0


def findLocation(idx: int):
    global count
    if idx == N:
        count += 1
        return
    else:
        for i in range(N):
            board[idx] = i  # 가능한지 하나씩 다 놓아보자
            if isOkay(idx):  # 현재 행을 정한게 알맞은 행동인지 체크
                findLocation(idx+1)  # 현재 행이 정해졌으니 다음 행을 정해야 함.


findLocation(0)
print(count)
