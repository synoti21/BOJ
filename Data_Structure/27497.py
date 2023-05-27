import sys
from collections import deque

input = sys.stdin.readline
but_deque = deque()

n = int(input())
last_put = []
for i in range(n):
    comm = list(map(str,input().split()))
    if comm[0] == '1':
        but_deque.append(comm[1])
        last_put.append(1)
    elif comm[0] == '2':
        but_deque.appendleft(comm[1])
        last_put.append(0)
    elif comm[0] == '3':
        if len(but_deque) > 0:
            if last_put[-1] == 0:
                but_deque.popleft()
            elif last_put[-1] == 1:
                but_deque.pop()
            last_put.pop()
if len(but_deque) > 0:
    while len(but_deque) > 0:
        print(but_deque.popleft(),end ="")
else:
    print(0)