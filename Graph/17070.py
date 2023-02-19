import sys
from collections import deque

input = sys.stdin.readline

d = [(0,1),(1,0),(1,1)]

N = int(input())
graph = [[] for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

queue = deque()
queue.append((1,0,0))
cnt = 0

def check(x,y,spin):
    if spin == 0:
        dx = x + 1
        dy = y
        if 0 <= dx < N and 0 <= dy < N and graph[dy][dx] == 0:
            return 1
        else:
            return 0
    elif spin == 1:
        dx = x
        dy = y + 1
        if 0 <= dx < N and 0 <= dy < N and graph[dy][dx] == 0:
            return 1
        else:
            return 0
    elif spin == 2:
        dx = x + 1
        dy = y + 1
        if 0 <= dx < N and 0 <= dy < N and graph[dy][dx] == 0 and graph[dy-1][dx] == 0 and graph[dy][dx-1] == 0:
            return 1
        else:
            return 0

while True:
    x,y,spin = queue.popleft()
    if x == N-1 and y == N-1:
        cnt +=1
        continue
    if spin == 0:
        if check(x,y,0):
            queue.append((x+1,y,0))
        if check(x,y,2):
            queue.append((x+1,y+1,2))
    elif spin == 1:
        if check(x,y,1):
            queue.append((x,y+1,1))
        if check(x,y,2):
            queue.append((x+1,y+1,2))
    elif spin == 2:
        if check(x, y, 0):
            queue.append((x + 1, y, 0))
        if check(x, y, 1):
            queue.append((x, y + 1, 1))
        if check(x, y, 2):
            queue.append((x + 1, y + 1, 2))

print(cnt)