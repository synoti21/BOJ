def find(a, parent):
    if a == parent[a]:
        return a
    pa = find(parent[a], parent)
    parent[a] = pa
    return parent[a]

def union(a, b, rank, parent, p_dict, cycle):
    a = find(a, parent)
    b = find(b, parent)
    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1


def test(n, m, p_dict, case):
    parent = [i for i in range(n + 1)]
    rank = [0 for _ in range(n + 1)]
    cycle = []

    for i in range(m):
        a, b = map(int, input().split())
        pa = find(a, parent)
        pb = find(b, parent)
        if pa != pb:
            union(a, b, rank, parent, p_dict, cycle)
        else:
            cycle.append(a)
    for i in range(n+1):
        find(i, parent)
    p_set = set()
    for cv in cycle:
        p_set.add(parent[cv])

    ans = 0
    for i in range(1, n+1):
        if parent[i] in p_set:
            continue
        ans += 1
        p_set.add(parent[i])

    if ans > 1:
        print(f'Case {case}: A forest of {ans} trees.')
    elif ans == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: No trees.')


case = 1
while True:
    n, m = map(int, input().split())
    p_dict = {i: False for i in range(0, n + 1)}
    if n == 0 and m == 0:
        exit()
    test(n, m, p_dict, case)
    case += 1