#일단 가장 낮은 것 부터 더해야 중복으로 더할 때 가장 수가 적다.
#그럼 최대한 낮은 값부터 더하는 게 좋음 -> 우선순위 큐
import heapq

n = int(input())
heap = []
arr = []

for i in range(n):
    card = int(input())
    heapq.heappush(heap, card)

for _ in range(n-1):
    prev = heapq.heappop(heap)
    cur = heapq.heappop(heap)
    sum = prev+cur
    heapq.heappush(heap, sum)
    arr.append(sum)

ans = 0

for i in arr:
    ans += i
print(ans)