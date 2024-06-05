import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[] for _ in range(n)]
sum_arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int,input().split()))

sum_arr[0][0] = arr[0][0]
for i in range(1,n):
    sum_arr[0][i] = sum_arr[0][i-1] + arr[0][i]

for i in range(1,n):
    sum_arr[i][0] += sum_arr[i-1][0] + arr[i][0]
    for j in range(1,n):
        sum_arr[i][j] = sum_arr[i-1][j] + sum_arr[i][j-1] + arr[i][j] - sum_arr[i-1][j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    if x1 == 1:
        if y1 == 1:
            print(sum_arr[x2-1][y2-1])
        else:
            print(sum_arr[x2 - 1][y2 - 1] - sum_arr[x2 - 1][y1 - 2])
    else:
        if y1 == 1:
            print(sum_arr[x2 - 1][y2 - 1] - sum_arr[x1 - 2][y2 - 1])
        else:
            print(sum_arr[x2 - 1][y2 - 1] - sum_arr[x1 - 2][y2 - 1] - sum_arr[x2 - 1][y1 - 2] + sum_arr[x1 - 2][y1 - 2])
# 1 3 6 10
# 2 5 9 14
# 3 7 12 18
# 4 9 15 22
#
# 1 3 6 10
# 3 8 15 24
# 6 15 27 42
# 10 24 42 66
#
# 27
#
# a b c d
# e f g h
# i j k l
#
# a        a+b           a+b+c               a+b+c+d
# a+e    a+b+e+f        a+b+c+e+f+g          a+b+c+d+e+f+g+h
# a+e+i   a+b+e+f+i+j   a+b+c+e+f+g+i+j+k    a+b+c+d+e+f+g+h+i+j+k+l

# dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
