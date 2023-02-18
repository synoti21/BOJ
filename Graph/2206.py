import sys
from collections import deque

d = [(1,0),(-1,0),(0,1),(0,-1)]
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
queue = deque()

visited[0][0][0] = 1
queue.append((0,0,0))

def bfs(sx,sy,w):
    visited[sy][sx][w] = 1
    queue.append((sy, sx, w))
    while queue:
        y,x,w = queue.popleft()
        if y == N-1 and x == M-1:
            return visited[y][x][w]
        for i in d:
            dx = x + i[1]
            dy = y + i[0]
            if 0 <= dx < M and 0 <= dy < N:
                if graph[dy][dx] == 1 and w == 0:
                    visited[dy][dx][1] = visited[y][x][0] + 1
                    queue.append((dy, dx, 1))
                elif graph[dy][dx] == 0 and visited[dy][dx][w] == 0:
                    visited[dy][dx][w] = visited[y][x][w] + 1
                    queue.append((dy,dx, w))

    return -1

print(bfs(0,0,0))