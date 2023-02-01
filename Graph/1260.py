def dfs(v):
    print(v, end = " ")
    visited[v] = 1
    for i in sorted(graph[v]):
        if(visited[i] == 0):
            visited[i] = 1
            dfs(i)
def bfs(v):
    print(v, end = " ")
    queue.append(v)
    visited[v] = 1
    while(queue):
        x = queue.pop(0)
        for i in sorted(graph[x]):
            if(visited[i] == 0):
                print(i, end = " ")
                visited[i] = 1
                queue.append(i)

N, V, M = map(int, input().split())
graph = [[]*N for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
queue = []


if __name__ == '__main__':

    for _ in range(V):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    dfs(M)
    print()
    visited = [0 for _ in range(N+1)]
    bfs(M)

