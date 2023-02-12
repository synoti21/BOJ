import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
heap = []
noway = 0

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

va, vb = map(int,input().split())

def sol(start, end):
    global noway
    table = [INF] * (N + 1)
    table[start] = 0
    heapq.heappush(heap,(0, start))
    flag = 0

    while heap:
        wei, now_node = heapq.heappop(heap)
        if now_node == end: flag = 1
        for w, next_node in graph[now_node]:
            next_w = w+wei
            if table[next_node] > + next_w:
                table[next_node] = next_w
                heapq.heappush(heap, (next_w, next_node))
    if flag:
        return table[end]
    else:
        noway = 1
        return -1

dis1 = sol(1, va) + sol(va,vb) + sol(vb, N)
dis2 = sol(1, vb) + sol(vb,va) + sol(va, N)

if noway == 1:
    print(-1)
elif dis1 > dis2:
    print(dis2)
else:
    print(dis1)