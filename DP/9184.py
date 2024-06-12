dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        dp[0][i][j] = 1
        dp[i][0][j] = 1
        dp[i][j][0] = 1
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        exit(0)
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")