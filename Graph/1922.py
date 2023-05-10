import heapq
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([c,a,b])
    graph[b].append([c,b,a])

def sol(start):
    global visited

    s_edges = graph[start]
    heapq.heapify(s_edges)
    visited[start] = 1
    total = 0

    while s_edges:
        wei, start, end = heapq.heappop(s_edges)
        if visited[end] == 0:
            visited[end] = 1
            total += wei
            for edge in graph[end]:
                if visited[edge[2]] == 0:
                    heapq.heappush(s_edges,edge)
    return total

print(sol(1))







