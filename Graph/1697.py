from collections import deque

def move(p,w):
    if w == 0:
        return p+1
    elif w == 1:
        return p-1
    elif w == 2:
        return p*2
def sol():
    global N,K
    queue = deque()
    queue.append(N)
    while queue:
        p = queue.popleft()
        if(p == K):
            return graph[p]
        for i in range(3):
            dp = move(p,i)
            if 0 <= dp <= 100000 and graph[dp] == 0:
                graph[dp] = graph[p]+1
                queue.append(dp)




N, K = map(int, input().split())
graph = [0] * (100001)
print(sol())