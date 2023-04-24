import sys
from collections import deque

input = sys.stdin.readline

r,c = map(int,input().split())
graph = [[] for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]

shp = 0
wlf = 0

d = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(r):
    graph[i] = list(map(str,input().strip()))

for i in range(r):
    for j in range(c):
        if graph[i][j] == '.':
            graph[i][j] = 0
        elif graph[i][j] == '#':
            graph[i][j] = -1
        elif graph[i][j] == 'o':
            graph[i][j] = 1
            shp += 1
        elif graph[i][j] == 'v':
            graph[i][j] = 2
            wlf += 1

def bfs(br,bc):
    global visited,shp,wlf

    b_wlf = 0
    b_shp = 0

    queue = deque()
    queue.append((br,bc))
    visited[br][bc] = 1

    if graph[br][bc] == 1:
        b_shp += 1
    elif graph[br][bc] == 2:
        b_wlf += 1


    while queue:
        nr,nc = queue.pop()
        for mv in d:
            d_r = nr+mv[0]
            d_c = nc+mv[1]
            if 0 <= d_r< r and 0 <= d_c < c and visited[d_r][d_c] == 0 and graph[d_r][d_c] != -1:
                if graph[d_r][d_c] == 1:
                    b_shp += 1
                elif graph[d_r][d_c] == 2:
                    b_wlf += 1
                visited[d_r][d_c] = 1
                queue.append((d_r,d_c))

    if b_shp > b_wlf:
        wlf -= b_wlf
    else:
        shp -= b_shp

for i in range(r):
    for j in range(c):
        if graph[i][j] != -1 and visited[i][j] == 0:
            bfs(i,j)

print(str(shp) + " " + str(wlf))