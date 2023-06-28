import heapq
n,s = map(int,input().split())
p_arr = [0 for _ in range(n+1)]
arr = list(map(int,input().split()))
for i in range(1,n+1):
    p_arr[i] = p_arr[i-1] + arr[i-1]

cand = []
start = 0
end = 0

while end <= n:
    if start == end:
        if p_arr[end] >= s:
            heapq.heappush(cand,(1, start, end))
            end+=1
        else:
            end+=1
    else:
        if p_arr[end]-p_arr[start] >= s:
            heapq.heappush(cand,(end-start, start, end))
            start += 1
        else:
            end += 1

if len(cand) > 0:
    ans, start, end = heapq.heappop(cand)
    print(ans)
else:
    print(0)