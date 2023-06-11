import heapq
m,n = map(int,input().split())
maze = [[] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
ans = []
heap = []

d = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(n):
    maze[i] = list(map(int,input().strip()))

heapq.heappush(heap, [0,0,0])
visited[0][0] = 1

while heap:
    count, row, col = heapq.heappop(heap)
    if row == n-1 and col == m-1:
        ans.append(count)
    for mv in d:
        d_row = row + mv[0]
        d_col = col + mv[1]
        if 0 <= d_row < n and 0 <= d_col < m and visited[d_row][d_col] == 0:
            if maze[d_row][d_col] == 0:
                heapq.heappush(heap,[count,d_row, d_col])
                visited[d_row][d_col] = 1
            else:
                heapq.heappush(heap,[count+1,d_row,d_col])
                visited[d_row][d_col] = 1

print(sorted(ans)[0])