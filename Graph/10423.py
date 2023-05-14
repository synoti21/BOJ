#MST의 원리를 사용하는 것일 뿐, MST를 만드는 문제는 아니다.
#애초에 시작지점이 여러개일 뿐더러, 시작지점에서 출발할 때, 더 큰 통로가 있으면 잘라내야 한다.
#다만 양방향처럼 보이지만 시작지점이 분명하게 정해져 있으므로 사실상 단방향
#시작지점이 있으므로 프림 알고리즘이 적절
#각 노드에는 자신이 도착 지점일 때의 그때까지 걸리는 거리의 최소값이 정해져있다.
#그럼 노드별로 최소값을 저장하고, 그게 갱신되면 새로고침한다.
#그래프는 [비용, 시작, 도착, 누적 거리]를 저장한다.

#근데.....생각해보니 그냥 간선만 연결하면 되네...?
#프림이 아니라 오히려 크루스컬이 맞다.
#어차피 간선 비용대로 정렬할 것이고, 이론상 비용이 적은 간선부터 연결될 것이 뻔하다.
#단, 쓸대없는 union을 방지하기 위해 find를 통해 만일 최상위 루트가 발전소 중 하나라면 union하지 않는다. => 새로운 조건 (골드2인 이유)

import sys
INF = sys.maxsize

n,m,k = map(int,input().split())
fac = list(map(int,input().split()))
edges = [[] for _ in range(m)]
parent = [0 for _ in range(n+1)]
rank = [0 for _ in range(n+1)]

for i in range(m):
    u,v,w = map(int,input().split())
    edges[i] = [w,u,v]

for i in range(n+1):
    parent[i] = i

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

    if a in fac:
        parent[b] = a
        return
    elif b in fac:
        parent[a] = b
        return

    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1

def sol():
    global edges
    edges.sort()

    total = 0

    for edge in edges:
        cost, start, end = edge
        if not edge:
            continue
        ps = find(start)
        pe = find(end)
        if ps != pe:
            if (ps in fac) and (pe in fac):
                continue
            union(start,end)
            total += cost
    return total

print(sol())