import sys

INF = sys.maxsize
input = sys.stdin.readline
n,m,r = map(int,input().split())
item = list(map(int,input().split()))
dp = [[INF for _ in range(n)] for _ in range(n)]
for _ in range(r):
    a,b,l = map(int,input().split())
    dp[a-1][b-1] = l
    dp[b-1][a-1] = l

for i in range(n):
    dp[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ans = [0 for _ in range(n)]
for i in range(n):
    sum = 0
    for j in range(n):
        if dp[i][j] <= m:
            sum += item[j]
    ans[i] = sum
print(sorted(ans, reverse=True)[0])