import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
    comm = list(map(str,input().split()))
    if comm[0] == "push_front":
        queue.appendleft(int(comm[1]))
    elif comm[0] == "push_back":
        queue.append(int(comm[1]))
    elif comm[0] == "pop_front":
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif comm[0] == "pop_back":
        if len(queue) > 0:
            print(queue.pop())
        else:
            print(-1)
    elif comm[0] == "size":
        print(len(queue))
    elif comm[0] == "empty":
        if len(queue) <= 0:
            print(1)
        else:
            print(0)
    elif comm[0] == "front":
        if len(queue) <= 0:
            print(-1)
        else:
            temp = queue.popleft()
            print(temp)
            queue.appendleft(temp)
    elif comm[0] == "back":
        if len(queue) <= 0:
            print(-1)
        else:
            temp = queue.pop()
            print(temp)
            queue.append(temp)


