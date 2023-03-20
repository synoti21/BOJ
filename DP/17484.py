dp = [[] for _ in range(7)]
n, m = map(int, input().split())
matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    matrix[i] = list(map(int,input().split()))

for i in range(4):
    dp[1][i] = matrix[i]

for i in range(4):
    dp[2][i] = 