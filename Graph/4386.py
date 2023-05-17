from math import sqrt
n = int(input())
vertex = []
edges = []
rank = [0 for _ in range(n)]
parent = [0 for _ in range(n)]
for i in range(n):
    x,y = map(float, input().split())
    vertex.append([x,y])

for i in range(n):
    parent[i] = i

for i in range(n-1):
    for j in range(i+1,n):
        edges.append([sqrt(pow(vertex[i][0] - vertex[j][0],2)+pow(vertex[i][1] - vertex[j][1],2)),i,j])

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
        return
    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1



def sol():
    edges.sort()
    total = 0
    for edge in edges:
        if not edge:
            continue
        wei, start, end = edge
        if find(start) != find(end):
            union(start,end)
            total += wei
    return total

print(round(sol(),2))
