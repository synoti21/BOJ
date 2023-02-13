import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

N, K = map(int, input().split())
heap = []
table = [INF] * 100001

def move(s, i):
    if i == 0:
        return (1, s+1)
    elif i == 1:
        return (1, s-1)
    elif i == 2:
        return (0, s*2)

def sol():
    heapq.heappush(heap, (N, 0))
    table[N] = 0

    while heap:
        now_node, wei = heapq.heappop(heap)
        for x in range(3):
            w, new_node = move(now_node, x)
            new_w = w + wei
            if 0 <= new_node <= 100000 and table[new_node] > new_w:
                table[new_node] = new_w
                heapq.heappush(heap, (new_node, new_w))
sol()
print(table[K])