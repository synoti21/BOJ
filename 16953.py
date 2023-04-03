from collections import deque

a,b = map(int, input().split())
queue = deque()
queue.append((a,1))

def compute(x,n):
    if n == 0:
        return x*2
    elif n == 1:
        return x*10+1

cnt = 0
flag = 0
while queue:
    x, trav = queue.pop()
    if x == b:
        flag = 1
        cnt = trav
        break
    for i in range(2):
        new_x = compute(x,i)
        if new_x <= b:
            queue.append((new_x, trav+1))
        else:
            continue
if flag:
    print(cnt)
else:
    print(-1)





