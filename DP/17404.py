import sys
INF = sys.maxsize
n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n)]
arr = [[0 for _ in range(3)] for _ in range(n)]
ans = INF

for i in range(n):
    arr[i] = list(map(int,input().split()))

for k in range(3): # 첫번째 집이랑 마지막 집이랑 이웃하면 안되므로 첫번째 집 색깔을 세가지 색으로 고정
    for i in range(3): # 이를 위해 첫번째 집을 칠할 때, 나머지는 무한으로 고정
        if i == k:
            dp[0][i] = arr[0][i]
        else:
            dp[0][i] = INF
    for i in range(1,n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

    for i in range(3):
        if i == k: #이웃하면 패스
            continue
        else:
            ans = min(ans, dp[n-1][i])
print(ans)