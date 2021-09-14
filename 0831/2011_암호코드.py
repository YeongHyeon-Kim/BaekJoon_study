import sys
input=sys.stdin.readline

sec = list(input().strip())

len_sec = len(sec)
if sec[0] == "0":
    print(0)

else:
    dp = [0 for _ in range(len_sec+1)]
    dp[0], dp[1] = 1, 1
    for i in range(2, len_sec+1):
        if int(sec[i-1]) > 0: # 0 처리
            dp[i] += dp[i-1] # 숫자 1개짜리는 앞에 만든 경우의 수 그대로 따라감
        combi_num = int(sec[i-1]) + int(sec[i-2])*10        
        if 10 <= combi_num <=26:
            dp[i] += dp[i-2] # 앞숫자와 조합해서 조건에 맞으면 앞앞 수의 경우까지를 다시 만들수있음

    print(dp[len_sec]%1000000)
        
