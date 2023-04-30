n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp_rev = [0 for _ in range(n)]

dp[0] = 1
dp_rev[-1] = 1

for i in range(n):
    val = 0
    for j in range(i):
        if arr[i] > arr[j] and dp[j] > val:
            val = dp[j]
    dp[i] = val+1

for i in range(n-1,-1,-1):
    val_rev = 0
    for j in range(n-1,i,-1):
        if arr[i] > arr[j] and dp_rev[j] > val_rev:
            val_rev = dp_rev[j]
    dp_rev[i] = val_rev + 1

for i in range(n):
    dp[i]+=dp_rev[i]-1

print(sorted(dp,reverse=True)[0])


