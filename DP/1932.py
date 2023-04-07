n = int(input())
arr = [[] for _ in range(n)]
dp = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int,input().split()))

dp[0].append(arr[0][0])

for i in range(1, n):
    dp[i].append(dp[i-1][0] + arr[i][0])
    for j in range(1,i):
        dp[i].append(max(dp[i-1][j-1]+arr[i][j], dp[i-1][j]+arr[i][j]))
    dp[i].append(dp[i-1][i-1] + arr[i][i])

print(max(dp[n-1]))

