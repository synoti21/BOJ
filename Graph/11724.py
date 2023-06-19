from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

count = 0

def bfs(start):
    global visited, count

    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        now = queue.pop()
        for new_node in graph[now]:
            if visited[new_node] == 0:
                queue.append(new_node)
                visited[new_node] = 1

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    if visited[i] == 0:
        bfs(i)
        count += 1
print(count)