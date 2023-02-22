import sys

input = sys.stdin.readline

x = '-1'

while True:
    x = str(input().strip())
    if(x == '0'):
        break
    pel = 1
    for i in range(len(x)//2):
        if x[i] != x[len(x)-i-1]:
            pel = 0
            break
    if pel:
        print("yes")
    else:
        print("no")