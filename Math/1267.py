import sys

input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
Y, M = 0, 0
for i in l:
    Y += (i//30)*10 + 10
    M += (i//60)*15 + 15

if Y > M:
    print("M " + str(M))
elif Y < M:
    print("Y " + str(Y))
else:
    print("Y M " + str(Y))