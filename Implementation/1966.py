import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = deque()
    doc_dic = {}
    doc_list = list(map(int, input().split()))
    for i in range(N):
        doc_dic[i] = doc_list[i]
        queue.append(i)
    cnt = 0
    while queue:
        x = queue.popleft()
        if max(doc_dic.values()) == doc_dic[x]:
            if x == M:
                print(cnt+1)
                break
            else:
                doc_dic.pop(x)
                cnt += 1
        else:
            queue.append(x)






