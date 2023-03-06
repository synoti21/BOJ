import sys
from collections import deque
from math import *

input = sys.stdin.readline

R,C,T = map(int, input().split())
queue = deque()
d = [(1,0),(-1,0),(0,1),(0,-1)]
graph = [[] for _ in range(R)]
dst_list = []

for i in range(R):
    graph[i] = list(map(int, input().split()))
    for j in range(len(graph[i])):
        if graph[i][j] > 0:
            dst_list.append((i,j,graph[i][j]))

def spr():
    global dst_list

    d = [(1,0),(-1,0),(0,1),(0,-1)]
    for r,c,dst in dst_list:
        dst_sprd = floor(dst/5)
        for mv in d:
            dr = r + mv[0]
            dc = c + mv[1]
            if 0 <= dr < R and 0 <= dc < C:
                if not (dc == 0 and (dr == 2 or dr == 3)):
                    graph[r][c] -= dst_sprd
                    graph[dr][dc] += dst_sprd
    dst_list = []
    for r in range(R):
        for c in range(C):
            if graph[r][c] > 0:
                dst_list.append((r,c,graph[r][c]))




def clean():
    global dst_list

    graph[1][0] = graph[0][0]

    for i in range(1, C): #맨위 가로
        graph[0][i-1] = graph[0][i]

    graph[0][C - 1] = graph[1][C - 1] #중간 조절
    graph[1][C-1] = graph[2][C-1] #중간 조절



    for i in range(4, R-1): #아래 왼쪽
        graph[i][0] = graph[i+1][0]

    for i in range(1, C): #맨위 가로
        graph[R - 1][i - 1] = graph[R - 1][i]

    for i in range(R-1, 2, -1): #아래 오른쪽
        graph[i][C-1] = graph[i-1][C-1]



    for i in range(C-1, 1, -1): #공기청정기 가로
        graph[2][i] = graph[2][i-1]
        graph[3][i] = graph[3][i-1]

    graph[2][1] = 0
    graph[3][1] = 0

    dst_list = []
    for r in range(R):
        for c in range(C):
            if graph[r][c] > 0:
                dst_list.append((r, c, graph[r][c]))


for _ in range(T):
    spr()
    clean()

cnt = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] > 0:
            cnt += graph[i][j]

print(cnt)