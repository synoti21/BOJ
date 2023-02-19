import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((c,w))
    graph[c].append((p,w))

def dfs(start, w):
    visited[start] = w
    for new_node, wei in graph[start]:
        if visited[new_node] == -1:
            new_w = wei+w
            dfs(new_node, new_w)

dfs(1,0)
n_longest = visited.index(max(visited))
visited = [-1] * (n+1)
dfs(n_longest,0)
print(max(visited))
