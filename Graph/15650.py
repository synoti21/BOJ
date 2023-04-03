n,m = map(int,input().split())
visited = [0 for _ in range(n+1)]
arr = []

def sol(pos, depth):
    global visited,arr
    if depth == m:
        for i in arr:
            print(i, end = " ")
        print()

    for i in range(pos,n+1):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i)
            sol(i, depth+1)
            arr.pop()
            visited[i] = 0


sol(1,0)