n = int(input())
arr = list(map(int,input().split()))
stack = []
ans = [-1 for _ in range(n)]
stack.append((arr[0],0))

for i in range(1,n):
    while len(stack) > 0 and arr[i] > stack[-1][0]:
        num, index = stack.pop(-1)
        ans[index] = arr[i]
    stack.append((arr[i],i))
print(*ans)