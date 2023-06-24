# 철도가 연결될 때마다 행성들의 수를 출력해야 하므로, 철도가 연결되서 형성된 집합 내 행성 수 출력
# 각 집합 별로 행성의 갯수를 저장
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
planet = [0 for _ in range(n+1)]
parent = [i for i in range(n+1)]
p_count = {i:0 for i in range(n+1)}
rank = [0 for _ in range(n+1)]

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        print(p_count[a])
        return
    if rank[a] > rank[b]:
        parent[b] = a
        p_count[a] += p_count[b]
        print(p_count[a])
    else:
        parent[a] = b
        p_count[b] += p_count[a]
        if rank[a] == rank[b]:
            rank[b] += 1
        print(p_count[b])


for i in range(1,n+1):
    planet[i] = int(input())
    p_count[i] = planet[i]

for _ in range(m):
    f,s = map(int,input().split())
    union(f,s)





