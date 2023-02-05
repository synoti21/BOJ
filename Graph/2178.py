d = [(0,1),(0,-1),(1,0),(-1,0)]
def sol():
    visited[0][0] = 1
    graph[0][0] = 1
    queue = []
    queue.append((0,0))
    while(queue):
        x = queue.pop(0)
        if(x[0] == M-1 and x[1] == N-1):
            return graph[x[1]][x[0]]
        for i in range(4):
            dx = x[0] + d[i][0]
            dy = x[1] + d[i][1]
            if 0 <= dx < M and 0 <= dy < N and visited[dy][dx] == 0 and graph[dy][dx] != 0:
                visited[dy][dx] = 1
                graph[dy][dx] = graph[x[1]][x[0]] + 1
                queue.append((dx,dy))







N,M = map(int, input().split())
visited = [[0 for _ in range(M)] for _ in  range(N)]
graph = [list(map(int, input())) for _ in range(N)]

print(sol())



