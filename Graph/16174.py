n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    par, chi = map(str,input().split())
