def sol(s):
    global cnt
    queue = []
    visited[s] = 1
    queue.append(s)
    while(queue):
        x = queue.pop(0)
        for i in graph[x]:
            if(visited[i] == 0):
                queue.append(i)
                visited[i] = 1
                cnt+=1


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
