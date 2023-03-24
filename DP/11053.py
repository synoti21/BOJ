n = int(input())
dp = [0 for _ in range(n)]

enu = list(map(int, input().split()))
dp[0] = 1
for i in range(1,n):
    val = 0
    for j in range(i):
        if enu[i] > enu[j]:
            if dp[j] > val:
                val = dp[j]
    dp[i] = val+1
print(max(dp))