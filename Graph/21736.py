import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
s_r, s_c = -1,-1

queue = deque()

for i in range(n):
    graph[i] = list(map(str,input().strip()))
    if s_r == -1 and s_c == -1:
        for j in range(m):
            if graph[i][j] == 'I':
                s_r = i
                s_c = j

queue.append([s_r,s_c])
visited[s_r][s_c] = 1
d = [(1,0),(-1,0),(0,1),(0,-1)]
ans = 0
while queue:
    row, col = queue.popleft()
    for mv in d:
        d_row = row + mv[0]
        d_col = col + mv[1]
        if 0 <= d_row < n and 0 <= d_col < m and graph[d_row][d_col] != 'X' and visited[d_row][d_col] == 0:
            visited[d_row][d_col] = 1
            queue.append([d_row,d_col])
            if graph[d_row][d_col] == 'P':
                ans +=1
if ans > 0:
    print(ans)
else:
    print("TT")