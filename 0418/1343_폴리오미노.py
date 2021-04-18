board = list(input())
i=0



while(i<len(board)):
    if board[i] == '.':
        i+=1
    else:
        if ((board[i:i+4]).count('X')) != 4:
            if (board[i:i+2]).count('X') != 2:
                print(-1)
                break
            else:
                board[i] = 'B'
                board[i+1] = 'B'
                i+=2
        else:
            board[i] = 'A'
            board[i+1] = 'A'
            board[i+2] = 'A'
            board[i+3] = 'A'
            i+=4

if board.count('X')==0:            
    print(''.join(board))          
    
    