import sys
from collections import deque
input = sys.stdin.readline

K = int(input())

def bfs(s, l):
    queue = deque()
    queue.append(s)
    visited[s] = l
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = -visited[x]
            elif visited[i] == visited[x]:
                return False
    return True

for _ in range(K):
    ans = 0
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1,V+1):
        if visited[i] ==0:
            ans = bfs(i,1)
            if not ans:
                break
    if ans:
        print("YES")
    else:
        print("NO")




