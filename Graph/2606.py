def sol(s):
    global cnt
    visited[s] = 1
    for i in graph[s]:
        if(visited[i] == 0):
            cnt+=1
            sol(i)


cnt = 0
V = int(input())
E = int(input())
graph = [[]*V for _ in range(V+1)]
visited = [0]*(V+1)
for _ in range(E):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

sol(1)
print(cnt)
