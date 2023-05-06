c = int(input())
graph = [[]]
visited = [0 for _ in range(11)]
ans = []

def sol():
    global graph,visited
    graph = [[] for _ in range(11)]
    for i in range(11):
        graph[i] = list(map(int,input().split()))

    for i in range(11):
        visited[i] = 1
        bt(0,i,0)
        visited[i] = 0


def bt(player, num, sum):
    global visited

    if graph[player][num] < 1:
        return
    sum += graph[player][num]

    if player == 10:
        ans.append(sum)
        return

    for i in range(11):
        if visited[i] == 0:
            visited[i] = 1
            bt(player+1,i,sum)
            visited[i] = 0

for _ in range(c):
    sol()
    print(sorted(ans,reverse=True)[0])
    ans = []
    visited = [0 for _ in range(11)]