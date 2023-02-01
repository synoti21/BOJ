def sol():
    for i in range(N):
        for j in range(N):
            if (visited[i][j] == 0 and graph[i][j] == 1):
                bfs(i, j)


def bfs(row, col):
    global N, graph, visited, apt_list
    cnt = 1
    queue = []
    queue.append((row, col))
    visited[row][col] = 1
    while(queue):
        p = queue.pop(0)
        n_row = p[0]
        n_col = p[1]
        if(n_row > 0 and graph[n_row-1][n_col] == 1 and visited[n_row-1][n_col] == 0):
            visited[n_row-1][n_col] = 1
            queue.append((n_row-1, n_col))
            cnt+=1
        if (n_row < N-1 and graph[n_row+1][n_col] == 1 and visited[n_row + 1][n_col] == 0):
            visited[n_row + 1][n_col] = 1
            queue.append((n_row + 1, n_col))
            cnt += 1
        if (n_col > 0 and graph[n_row][n_col-1] == 1 and visited[n_row][n_col-1] == 0):
            visited[n_row][n_col-1] = 1
            queue.append((n_row, n_col-1))
            cnt += 1
        if (n_col < N-1 and graph[n_row][n_col+1] == 1 and visited[n_row][n_col+1] == 0):
            visited[n_row][n_col+1] = 1
            queue.append((n_row, n_col+1))
            cnt += 1
    apt_list.append(cnt)


if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    apt_list = []
    sol()
    print(len(apt_list))
    for i in sorted(apt_list):
        print(i)

