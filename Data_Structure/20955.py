import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]
cut = 0

def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a,b):
    global cut

    a = find(a)
    b = find(b)
    if a == b:
        cut += 1
        return
    if rank[a] > rank[b]:
        parent[b] = a
        rank[a] += 1
    else:
        parent[a] = b
        rank[b] += 1

for _ in range(m):
    u,v = map(int,input().split())
    union(u,v)

ans = []
for i in range(1,n+1):
    p = find(parent[i])
    ans.append(p)
print(len(set(ans))-1+cut)
