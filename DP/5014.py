import sys
from collections import deque

input = sys.stdin.readline
f,s,g,u,d = map(int, input().split())
visited = [0 for i in range(f+1)]
count = [0 for i in range(f+1)]

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == g:
            return count[g]
        for i in (v+u, v-d):
            if 0 < i <= f and not visited[i]:
                visited[i] = 1
                count[i] = count[v] + 1
                q.append(i)
    if count[g] == 0:
        return "use the stairs"

print(bfs(s))