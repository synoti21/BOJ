import sys
import heapq

input = sys.stdin.readline

n,c = map(int, input().split())
vertex = []
rank = [0 for _ in range(n)]
parent = [i for i in range(n)]
heap =[]
for i in range(n):
    x,y = map(float, input().split())
    vertex.append([x,y])


for i in range(n):
    for j in range(i+1,n):
        cost = (vertex[i][0] -vertex[j][0])**2 + (vertex[i][1] - vertex[j][1])**2
        if cost >= c:
            heapq.heappush(heap,[cost,i,j])

def find(a):
    if parent[a] == a:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    else:
        parent[b] = a
        return True

def sol():
    total = 0
    count = 0
    while heap:
        wei, start, end = heapq.heappop(heap)
        if union(start,end):
            total += wei
            count += 1
            if count == n-1:
                break
    if count == n-1:
        print(int(total))
    else:
        print(-1)

sol()