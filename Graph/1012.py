import sys
d = [(1,0),(-1,0),(0,1),(0,-1)]
sys.setrecursionlimit(10**6)
def sol():
    global M,N
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt+=1
    return cnt

def dfs(row,col):
    visited[row][col] = 1
    for i in range(4):
        dx = col + d[i][0]
        dy = row + d[i][1]
        if 0 <= dx < M and 0 <= dy < N and visited[dy][dx] == 0 and graph[dy][dx] == 1:
            dfs(dy,dx)



T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x,y = map(int, input().split())
        graph[y][x] = 1
    print(sol())

