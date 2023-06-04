import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n = 0
des_list = []
graph = [[]]
heap = []
table = []
sniff_way = 0

vg, vh = 0, 0 #반드시 지나는

T = int(input())

def sol(start, end):
    heapq.heappush(heap, (0, start))
    table = [INF] * (n+1)
    table[start] = 0
    eflag = 0

    while heap:
        wei, now_node = heapq.heappop(heap)
        if now_node == end:
            eflag = 1
        for w, new_node in graph[now_node]:
            new_w = w + wei
            if table[new_node] > new_w:
                table[new_node] = new_w
                heapq.heappush(heap, (new_w, new_node))

    if eflag == 1:
        return table[end]
    else:
        return -INF

for _ in range(T):

    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())


    vg = g
    vh = h
    start = s
    des_list = [0 for _ in range(t+1)]
    graph = [[] for _ in range(n+1)]
    heap = []
    table = [INF]*(n+1)

    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        if (a == vg and b == vh) or (a == vh and b == vg):
            sniff_way = d
        graph[a].append((d,b))
        graph[b].append((d,a))
    for i in range(t):
        x = int(sys.stdin.readline())
        des_list[i] = x

    dis_list = []

    for d in des_list:
        dis = sol(s, d)
        if dis >= 0:
            dis_list.append(d)



    for i in sorted(dis_list):
        print(i, end = " ")