from collections import deque

m,n,k = map(int,input().split())
rec = [((0,0),(0,0)) for _ in range(k)]
graph = [[0 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

d = [(1,0),(-1,0),(0,1),(0,-1)]
ans = []
count = 0


for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    rec[i] = ((x1,y1),(x2,y2))

for i in range(k):
    x1,y1 = rec[i][0]
    x2,y2 = rec[i][1]

    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1

def bfs(x,y):
    global visited,graph,ans

    queue = deque()
    queue.append((x,y))
    visited[y][x] = 1
    sum = 1

    while queue:
        nx,ny = queue.pop()
        for mv in d:
            dx = nx+mv[0]
            dy = ny+mv[1]
            if 0<=dx<n and 0<=dy<m and graph[dy][dx] == 0 and visited[dy][dx] == 0:
                visited[dy][dx] = 1
                queue.append((dx,dy))
                sum += 1

    ans.append(sum)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and visited[i][j] == 0:
            bfs(j,i)
            count+=1


print(count)
for i in sorted(ans):
    print(i,end = " ")






