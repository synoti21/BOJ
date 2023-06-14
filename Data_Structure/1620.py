import sys
input = sys.stdin.readline
n,m = map(int,input().split())

pokemon_num = {}
pokemon_ident = {}

for i in range(n):
    temp = str(input().strip())
    pokemon_num[i+1] = temp
    pokemon_ident[temp] = i+1

for _ in range (m):
    comm = str(input().strip())
    if comm.isdigit():
        print(pokemon_num[int(comm)])
    else:
        print(pokemon_ident[comm])