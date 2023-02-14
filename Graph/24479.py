import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N, M ,R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
count = [0 for _ in range(N+1)]

cnt = 0


for _ in  range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()

def dfs(s):
    global cnt
    visited[s] = 1
    cnt += 1
    count[s] = cnt

    for i in graph[s]:
        if(visited[i] == 0):
            dfs(i)
dfs(R)
for i in range(1,N+1):
    print(count[i])