n, m = map(int, input().split())
enum = sorted(list(map(int, input().split())))
visited = [0 for _ in range(n)]
arr = []


def sol(depth):
    if depth == m:
        for i in arr:
            print(i, end=" ")
        print()
        return None

    for i in range(n):
        num = enum[i]
        if visited[i] == 0:
            visited[i] = 1
            arr.append(num)
            sol(depth + 1)
            visited[i] = 0
            arr.pop()


sol(0)
