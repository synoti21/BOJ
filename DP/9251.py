import sys
input = sys.stdin.readline

fstr = str(input().rstrip())
sstr = str(input().rstrip())

dp = [[0 for _ in range(len(fstr))] for _ in range(len(sstr))]


for i in range(len(fstr)):
    for j in range(len(sstr)):
        if fstr[i] == sstr[j]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
        else:
            dp[i][j] = dp[i-1][j]

print(dp)

