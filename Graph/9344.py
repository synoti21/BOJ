t = int(input())
edges = []
rank = []
parent = []


def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        return
    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1

def sol(p,q):
    edges.sort()
    flag = 0
    for edge in edges:
        if not edge:
            continue
        cost, start, end = edge
        if find(start) != find(end):
            union(start,end)
            if (start == p and end == q) or (start == q and end == p):
                flag = 1
    if flag:
        print("YES")
    else:
        print("NO")

for _ in range(t):
    n,m,p,q = map(int,input().split())
    rank = [0 for _ in range(n+1)]
    parent = [0 for _ in range(n+1)]
    edges = []

    for _ in range(m):
        u,v,w = map(int,input().split())
        edges.append([w,u,v])

    for i in range(n+1):
        parent[i] = i

    sol(p,q)