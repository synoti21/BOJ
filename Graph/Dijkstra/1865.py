import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

TC = int(input())
graph = [[]]
table = []
heap = []

def sol():
    table[1] = 0
    heapq.heappush(heap, (0, 1))
    prob_dis = []

    while heap:
        wei, now_node = heapq.heappop(heap)
        for new_node, w in graph[now_node]:
            new_w = wei+w
            if table[new_node] > new_w:
                table[new_node] = new_w
                if new_node == 1:
                    prob_dis.append(new_w)
                else:
                    heapq.heappush(heap, (new_w, new_node))
            elif new_node == 1:
                prob_dis.append(new_w)
    if len(prob_dis):
        return sorted(prob_dis)[0]
    else:
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

