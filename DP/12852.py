n = int(input())
dp = [[0,0],[0,0]]
ans = []

for i in range(2):
    dp.append([1,1])

for i in range(4,n+1):
    temp = []
    if i%3 == 0:
        temp.append([dp[i//3][0]+1,i//3])
    if i%2 == 0:
        temp.append([dp[i//2][0]+1,i//2])
    temp.append([dp[i-1][0]+1, i-1])

    dp.append(sorted(temp)[0])

def find(index):
    global ans

    if dp[index][1] == 0:
        return

    ans.append(dp[index][1])
    find(dp[index][1])

print(dp[n][0])
ans.append(n)
find(n)
print(*ans)