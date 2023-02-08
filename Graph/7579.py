from collections import deque
d = [(0,1),(0,-1),(1,0),(-1,0)]

M,N,T = map(int, input().split())
graph = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(T)]
t_cnt = 0
day = 0
rt_list = []

print(graph)

for i in range(T):
    for j in range(N):
        graph[i][j] = list(map(int, input().split()))
        for k in range(M):
            if graph[i][j][k] != -1:
                t_cnt += 1
            if graph[i][j][k] == 1:
                rt_list.append([i, j, k])
print(rt_list)
