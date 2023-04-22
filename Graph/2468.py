import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

max = -1

for i in range(n):
    graph[i] = list(map(int,input().split()))

def bfs(row, col, m_rain):
    global visited

    queue = deque()
    queue.append((row,col))

    while queue:
        r,c = queue.pop()
        for mv in d:
            d_row = r+mv[0]
            d_col = c+mv[1]
            if 0 <= d_row < n and 0 <= d_col < n and graph[d_row][d_col] > m_rain and visited[d_row][d_col] == 0:
                queue.append((d_row,d_col))
                visited[d_row][d_col] = 1

for i in range(n):
    for j in range(n):
        if graph[i][j] > max:
            max = graph[i][j]

cnt = [0 for _ in range(max+1)]

for rain in range(0,max+1):
    sum = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain and visited[i][j] == 0:
                bfs(i,j, rain)
                sum+=1
    cnt[rain] = sum
    visited = [[0 for _ in range(n)] for _ in range(n)]

print(sorted(cnt,reverse=True)[0])