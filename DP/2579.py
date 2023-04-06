n = int(input())
arr = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
    arr[i] = int(input())

dp[1] = arr[1]
if(n > 1):
    dp[2] = arr[1]+arr[2]
    if(n > 2):
        dp[3] = max(arr[1], arr[2]) + arr[3]

for i in range(4, n+1):
    dp[i] = max(arr[i] + dp[i-2], arr[i]+arr[i-1] + dp[i-3])
print(dp[n])