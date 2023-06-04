import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

mv = [(1,0),(-1,0),(0,1),(0,-1)]

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
table = [[INF for _ in range(N)] for _ in range(N)]
heap = []

table[0][0] = 0
visited[0][0] = 1
heapq.heappush(heap, (0,(0,0)))

while heap:
    wei, now = heapq.heappop(heap)
    for i in mv:
        dy = now[0] + i[0]
        dx = now[1] + i[1]
        if 0 <= dx < N and 0 <= dy < N and visited[dy][dx] == 0:
            visited[dy][dx] = 1
            if graph[dy][dx] == 1 and table[dy][dx] > wei:
                table[dy][dx] = wei
                heapq.heappush(heap, (wei, (dy,dx)))
            elif graph[dy][dx] == 0 and table[dy][dx] > wei:
                table[dy][dx] = wei+1
                heapq.heappush(heap, (wei+1, (dy, dx)))

print(table[N-1][N-1])