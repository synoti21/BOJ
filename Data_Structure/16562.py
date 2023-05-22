import sys

INF = sys.maxsize
n,m,k = map(int,input().split())
f_cost = list(map(int,input().split()))
f_cost.insert(0,0)
parent = [[i,f_cost[i]] for i in range(n+1)]

def find(a):
    if parent[a][0] == a:
        return a
    p = find(parent[a][0])
    parent[a][0] = p
    return parent[a][0]

def union(a,b):
    a = find(a)
    b = find(b)

    cost_a = parent[a][1]
    cost_b = parent[b][1]

    min_cost = min(cost_a, cost_b)
    if a == b:
        return
    else:
        parent[a][0] = b
        parent[a][1] = min_cost
        parent[b][1] = min_cost

for _ in range(m):
    v,w = map(int,input().split())
    union(v,w)


ans = []
sum_cost = 0
for i in range(len(parent)):
    p = find(parent[i][0]) #분리 집합 문제는 항상 최상위 노드를 기준으로 판단해야 한다. 꼭 최상위 노드를 찾는 것을 잊지 않아야 함.

    if p not in ans:
        sum_cost += parent[p][1]
        ans.append(parent[p][0])

if k >= sum_cost:
    print(sum_cost)
else:
    print("Oh no")
