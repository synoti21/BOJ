n, m = map(int, input().split())
sum = 1
div = 1
for i in range(n,(n-m),-1):
    sum *= i

for i in range(m,0,-1):
    div *= i

print(sum//div)