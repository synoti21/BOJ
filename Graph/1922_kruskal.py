import sys
sys.setrecursionlimit(10**6)
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
edges = [[] for _ in range(m)]
parent = [0 for _ in range(n+1)]
rank = [0 for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    edges[i] = [c,a,b]

for i in range(n+1):
    parent[i] = i

def find(a):
    if parent[a] == a:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a,b):
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return
    if rank[pa] > rank[pb]: #pa, a주의. 최상위 노드를 기준으로 찾는 것임.
        parent[pb] = pa
        rank[pa] += 1
    else:
        parent[pa] = pb
        if rank[pa] == rank[pb]:
            rank[pb] += 1



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

print(sol())

