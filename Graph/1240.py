from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,cost = map(int,input().split())
    graph[a].append([cost,b])
    graph[b].append([cost,a])

def sol(start, end):
    visited = [0 for _ in range(n+1)]
    queue = deque()

    visited[start] = 1
    queue.append((start,0))

    while queue:
        cur, cost = queue.popleft()
        if cur == end:
            print(cost)
            return
        for c, next in graph[cur]:
            if visited[next] == 0:
                visited[next] = 1
                queue.append((next, cost+c))

for _ in range(m):
    s,f = map(int,input().split())
    sol(s,f)