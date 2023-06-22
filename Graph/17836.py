#그람 안 얻고 목표까지 가기 vs 그람 얻고 바로 직진
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

n,m,t = map(int,input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int,input().split()))

d = [(1,0),(-1,0),(0,1),(0,-1)]

queue = deque()
queue.append([0,0,0]) #row,col,count, gram
visited[0][0] = 1

ans = []

while queue:
    row, col, count = queue.popleft() #popleft, pop 억까 1
    if graph[row][col] == 2:
        ans.append(count + (n-row-1) + (m-col-1))
        continue
    for mv in d:
        d_row = row + mv[0]
        d_col = col + mv[1]
        if 0 <= d_row < n and 0 <= d_col < m and graph[d_row][d_col] != 1:
            if d_row == n - 1 and d_col == m - 1:
                ans.append(count+1)
                continue
            if graph[d_row][d_col] == 0 and visited[d_row][d_col] == 0:
                visited[d_row][d_col] = 1
                queue.append([d_row, d_col, count+1])
            elif graph[d_row][d_col] == 2:
                queue.append([d_row,d_col, count+1])

if len(ans) == 0 or sorted(ans)[0] > t:
    print("Fail") #fail 대문자 억까 2 ㅅㅂㅅㅂㅅㅂㅅㅂ
else:
    print(sorted(ans)[0])