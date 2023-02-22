import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int,input().split())
    dis = y - x
    cnt = 0
    move = 1
    pos = 0
    while pos < dis :
        cnt += 1
        pos += move
        if cnt % 2 == 0 :
            move += 1  
    print(cnt)