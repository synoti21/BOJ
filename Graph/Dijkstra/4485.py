import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

d = [(1,0),(-1,0),(0,1),(0,-1)]

graph = [[]]
table = [[]]
heap = []

def sol(N):
    table[0][0] = graph[0][0]
    heapq.heappush(heap, (graph[0][0],(0,0)))
    while heap:
        wei, now_node = heapq.heappop(heap)
        for mv in d:
            dx = now_node[1] + mv[1]
            dy = now_node[0] + mv[0]
            if 0 <= dx < N and 0 <= dy < N:
                new_w = wei + graph[dy][dx]
                if table[dy][dx] > new_w:
                    table[dy][dx] = new_w
                    heapq.heappush(heap, (new_w, (dy,dx)))
    return table[N-1][N-1]

t = 1
while True:
    N = int(input())
    if N == 0: break

    graph = [[0 for _ in range(N)] for _ in range(N)]
    table = [[INF for _ in range(N)] for _ in range(N)]
    for i in range(N):
        graph[i] = list(map(int, input().split()))
    print("Problem " + str(t) + ": " + str(sol(N)))
    t+=1

