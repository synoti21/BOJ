from collections import deque
import sys

INF = sys.maxsize

N, M = map(int, input().split())
d = [1, 2, 3, 4, 5, 6]
graph = [INF for _ in range(101)]
jump = [0 for _ in range(101)]
queue = deque()
queue.append(1)

for _ in range(N):
    a, b = map(int, input().split())
    jump[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    jump[a] = b

graph[1] = 0
while(queue):
    cur = queue.popleft()
    for i in d:
        new_cur = cur
        new_cur += i
        if 1<=new_cur<=100:
            if jump[new_cur] != 0:
                temp = new_cur
                new_cur = jump[temp]
            if graph[cur]+1 < graph[new_cur]:
                graph[new_cur] = graph[cur]+1

                queue.append(new_cur)

print(graph[100])




