import sys

input = sys.stdin.readline

K, N = map(int, input().split())
line = [0 for _ in range(K)]

for i in range(K):
    line[i] = int(input())
start, end = 1, max(line)

while start <= end:
    mid = (start+end)//2
    sum = 0
    for l in line:
        sum += l//mid
    if sum >= N:
        start = mid+1
    else:
        end = mid -1
print(end)




