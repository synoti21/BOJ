import sys

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
disf = [[0 for _ in range(N+1)] for _ in range(N+1)]
diss = [[0 for _ in range(N+1)] for _ in range(N+1)]


for _ in range(M):
    a, b = map(int, input().split())
    disf[a][b] = 1


for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if disf[i][k] ==1 and disf[k][j] == 1:
                disf[i][j] = 1

cnt = 0
for i in range(1,N+1):
    flag = 0
    for j in range(1,N+1):
        flag += disf[i][j] + disf[j][i]
    if flag == N-1:
        cnt+=1

print(cnt)