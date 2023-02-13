import sys

input = sys.stdin.readline

N, K = map(int, input().split())
c_list = []
for _ in range(N):
    c_list.append(int(input()))
sum = 0
i = 0
c_list = sorted(c_list,reverse=True)
while K!=0 and i<N:
    if(K >= c_list[i]):
        sum += K//c_list[i]
        K %= c_list[i]
        i+=1
    else:
        i+=1
print(round(sum))
