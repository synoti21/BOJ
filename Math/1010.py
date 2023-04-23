import math

t = int(input())

for i in range(t):
    e,w = map(int,input().split())
    print(math.comb(w,e))