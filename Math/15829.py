n,m = map(int, input().split())
x = n*m
l = n%m
while l!=0:
    n = m
    m = l
    l = n%m
print(m)
print(x//m)