import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
dis_list = [0 for _ in range(N)]

for _ in range(M):
    s,d,t = map(int, input().split())
    graph[s].append((d,t))

def sol(vs, vd):
    heap = []
    table = [INF] * (N+1)
    table[vs] = 0
    heapq.heappush(heap, (0, vs))

    while heap:
        wei, now_node = heapq.heappop(heap)
        if now_node == vd: break
        for new_node, w in graph[now_node]:
            new_w = wei+w
            if table[new_node] > new_w:
                table[new_node] = new_w
                heapq.heappush(heap, (new_w,new_node))
    return table[vd]

for i in range(1, N+1):
    dis_list[i-1] = sol(i,X) + sol(X,i)

print(sorted(dis_list,reverse=True)[0])