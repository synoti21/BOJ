from collections import deque

n = int(input())
graph = [[] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int,input().split()))

d = [(1,0),(0,1)]

def sol(sr, sc):
    global graph, visited

    if graph[sr][sc] == -1:
        print("HaruHaru")
        exit()

    nr = sr + graph[sr][sc]
    nc = sc + graph[sr][sc]
    if 0<= nr < n and visited[nr][sc] == 0:
        visited[nr][sc] = 1
        sol(nr,sc)
        visited[nr][sc] = 0
    if 0<= nc < n and visited[sr][nc] == 0:
        visited[sr][nc] = 1
        sol(sr, nc)
        visited[sr][nc] = 0

sol(0,0)
print("Hing")