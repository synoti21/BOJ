import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

TC = int(input())
graph = [[]]
table = []
heap = []

def sol():
    r_start = 0
    table[1] = 0
    heapq.heappush(heap, (0, 1))
    while heap:
        wei, now_node = heapq.heappop(heap)
        if now_node == 1 and r_start == 1:
            return table[1]
        for new_node, w in graph[now_node]:
            if new_node == 1:
                r_start = 1
            new_w = wei+w
            if table[new_node] > new_w:
                table[new_node] = new_w
                heapq.heappush(heap, (new_w, new_node))
    return 0

for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    table = [INF] * (N+1)
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))
    if sol() < 0:
        print("YES")
    else:
        print("NO")

