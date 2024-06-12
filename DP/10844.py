# 1의 경우
# 1,2,3,4,5,6,7,8,9

# 2*7 + 3
# 2의 경우
# 21, 12, 32, 23, 43, 54, 34, 65,45, 76, 56, 87, 67, 98, 78, 89, 10
# 3의 경우
#    i=0  i=1  i=2
# 0   0    1    1
# 1   1    1    2
# 2   1    2    3
# 3   1    2    4
# 4   1    2    4
# 5   1    2    4
# 6   1    2    4
# 7   1    2    4
# 8   1    2    3
# 9   1    1    2
# 위의 경우는 n으로 끝나는 수로 생각했다. 조금 바꿔서 시작하는 수로 해본다면?
#      0  1  2  3  4  5  6  7  8  9
# i=0  1  1  1  1  1  1  1  1  1  1
# i=1  1  2  2  2  2  2  2  2  2  1
# i=2  2  3  4  4  4  4  4  4  3  2
# i=3  3  6  7  8  8  8  8  7  6  3
# i=4  6  10  14 15 16 16 15 14 10 6
# i=5  0
# i=6  0
# i=7  0
# i=8  0
# i=9  0
# => 이전 배열에서 인접한 두 수의 값과 똑같다. 왜냐, 3자리 중 첫자리가 자신인 것을 제외하면 그 다음에 올 수는
# 자리-1 에서 인접한 두 수의 갯수와 같기 때문

n = int(input())
dp = [[i for i in range(10)] for _ in range(n)]

for i in range(10):
    dp[0][i] = 1


for i in range(1,n):
    dp[i][0] = dp[i-1][1]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][9] = dp[i-1][8]
print((sum(dp[n-1])-dp[n-1][0])%1000000000)