import sys
input = sys.stdin.readline

n, m = map(int,input().split())
num = list(map(int,input().split()))
p_sum = [0 for _ in range(n+1)]
for i in range(1,n+1):
    p_sum[i] = num[i-1] + p_sum[i-1]

for _ in range(m):
    i, j = map(int,input().split())
    if i == j:
        print(num[i-1])
    else:
        print(p_sum[j]-p_sum[i-1])