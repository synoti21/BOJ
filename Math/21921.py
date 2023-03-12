n,x = map(int, input().split())
visit = list(map(int, input().split()))

sum = 0
cnt = 0
for i in range(x):
    sum += visit[i]
max = sum
if sum:
    cnt = 1
else:
    cnt = 0

for i in range(x,n):
    sum -= visit[i-x]
    sum += visit[i]

    if sum > max:
        cnt = 1
        max = sum
    elif sum == max:
        cnt += 1

if max:
    print(max)
    print(cnt)
else:
    print("SAD")


