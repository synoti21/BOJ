n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = pow((x[0] - y[0]),2)

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            dp[i][j] = pow((x[i] - y[j]),2) + dp[i][j-1]
        elif j == 0:
            dp[i][j] = pow((x[i] - y[j]),2) + dp[i-1][j]
        else:
            dp[i][j] = pow((x[i] - y[j]),2) + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

print(dp[n-1][n-1])