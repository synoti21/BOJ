from collections import deque

queue = deque()

n,k = map(int,input().split())
for i in range(1,n+1):
    queue.append(i)

pos = 0
ans = []
for i in range(n):
    for j in range(k):
        temp = queue.popleft()
        if j != k-1:
            queue.append(temp)
        else:
            ans.append(temp)
print("<",end = "")
print(*ans,sep=", ",end=">")