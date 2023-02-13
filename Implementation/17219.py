import sys

input = sys.stdin.readline
idpw = {}
N, M = map(int,input().strip().split())

for _ in range(N):
    a,b = map(str, input().strip().split())
    idpw[a] = b
for _ in range(M):
    a = str(input().strip())
    print(idpw[a])
