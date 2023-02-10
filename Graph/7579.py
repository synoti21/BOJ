from collections import deque
d = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)] #z,y,x

M,N,T = map(int, input().split())
graph = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(T)]
t_cnt = 0
rt_cnt = 0
day = 0
rt_list = []

for i in range(T):
    for j in range(N):
        graph[i][j] = list(map(int, input().split()))
        for k in range(M):
            if graph[i][j][k] != -1:
                t_cnt += 1
            if graph[i][j][k] == 1:
                rt_list.append([i, j, k])

queue = deque()
for i in rt_list:
    rt_cnt += 1
    queue.append(i)

while queue:
    x = queue.popleft()
    day = graph[x[0]][x[1]][x[2]]
    for i in d:
        dx = x[2]+i[2]
        dy = x[1]+i[1]
        dz = x[0]+i[0]
        if 0 <= dx < M and 0 <= dy < N and 0 <= dz < T and graph[dz][dy][dx] == 0:
            graph[dz][dy][dx] = graph[x[0]][x[1]][x[2]] + 1
            queue.append((dz,dy,dx))
            rt_cnt += 1

if rt_cnt == t_cnt:
    print(day-1)
else:
    print(-1)

