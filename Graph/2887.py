n = int(input())
node = [[0,0,0,0] for _ in range(n)]
edge = [[0,0,0] for _ in range(3*(n-1))]
parent = [0 for _ in range(n)]
rank = [0 for _ in range(n)]

for i in range(n):
    x,y,z = map(int,input().split())
    node[i] = [x,y,z,i]

node.sort(key=lambda x : x[0])
for i in range(n-1):
    edge[i] = [abs(node[i][0] - node[i+1][0]),node[i][3],node[i+1][3]]
node.sort(key=lambda x : x[1])
for i in range(n-1):
    edge[n-1+i] = [abs(node[i][1] - node[i+1][1]),node[i][3],node[i+1][3]]

node.sort(key=lambda x : x[2])
for i in range(n-1):
    edge[2*(n-1)+i] = [abs(node[i][2] - node[i+1][2]),node[i][3],node[i+1][3]]


for i in range(n):
    parent[i] = i

def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return p

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

def sol(edges):
    edges.sort()
    total = 0

    for edge in edges:
        if not edge:
            continue
        cost, start, end = edge
        if find(start) != find(end):
            union(start,end)
            total += cost
    return total

print(sol(edge))

