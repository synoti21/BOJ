n = int(input())
stick = [0 for _ in range(n)]
stack = []
for i in range(n):
    stick[i] = int(input())
stack.append(stick[n-1])
cnt = 1
for i in range(n-2,-1,-1):
    if stick[i] > stack[-1]:
        stack.append(stick[i])
print(len(stack))