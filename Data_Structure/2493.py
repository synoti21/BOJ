n = int(input())
laser = list(map(int,input().split()))
stack = []
ans = [0 for _ in range(n)]

stack.append((laser[-1],n-1))

for i in range(len(laser)-1,-1,-1):
    if laser[i] > stack[-1][0]:
        while len(stack) > 0 and laser[i] > stack[-1][0]:
            height, index = stack.pop(-1)
            ans[index] = i + 1
        stack.append((laser[i],i))
    else:
        stack.append((laser[i],i))

print(*ans)




