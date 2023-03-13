n, m = map(int, input().split())
coin = [0 for _ in range(n)]

cnt = 0
def flip(r,c):
    for i in range(r+1):
        for j in range(c+1):
            if coin[i][j]:
                coin[i][j] = 0
            else:
                coin[i][j] = 1

for i in range(n):
    coin[i] = list(map(int, input().strip()))

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if coin[i][j]:
            flip(i,j)
            cnt+=1
print(cnt)