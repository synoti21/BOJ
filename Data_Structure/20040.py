import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n)]
rank = [0 for _ in range(n)]

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
        return True
    if rank[a] > rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        if rank[a] == rank[b]:
            rank[b] += 1
    return False

for i in range(m):
    a,b = map(int,input().split())
    if union(a,b):
        print(i+1)
        exit()
print(0)