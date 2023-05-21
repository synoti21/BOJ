#위상정렬 : 순서가 정해져 있는 작업을 차례대로 수행해야 할 때 사용해야 하는 알고리즘
#방향성 그래프이면서 사이클이 없어야 한다. 선수과목이 예시가 될 수 있음.
#진입차수 : 특정 노드로 들어오는 간선 갯수, 진출차수 : 특정 노드에서 나가는 간선 갯수

#진입차수가 0이라는 것은 해당 노드 전에 수행해야 할 노드가 없다는 말!
#즉, 진입차수가 0인 노드는 곧 수행해야 할 노드로, 순서에 넣는다.
#만약 진입차수가 존재하면, 그 노드로 진출했던 선수 노드를 먼저 실행해야 한다.

#이 알고리즘은 따라서 진입차수를 0인 노드를 탐색한다.
#순서에 넣기 전, 이 노드의 진출차수에 해당하는 간선을 제거한다. (순서에 넣었으니 간선을 정리해야하는 것이 맞다.)
import sys
from collections import deque

input = sys.stdin.readline

t= int(input())
build_time = []
graph = []
inDegree = []
sum_time = []
def test():
    global build_time, graph, sum_time,inDegree

    n,k = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    build_time = list(map(int,input().split()))
    build_time.insert(0,0)
    inDegree = [0] * (n+1)
    for _ in range(k):
        x,y = map(int,input().split())
        graph[x].append(y)
        inDegree[y] += 1
    w = int(input())
    sum_time = [build_time[i] for i in range(n+1)]
    sol(n,w)

def sol(n,w):
    queue = deque()

    for i in range(1,n+1):
        if inDegree[i] == 0:
            queue.append(i)

    while queue:
        now_n = queue.popleft()
        if now_n == w:
            print(sum_time[now_n])
            return
        for next_n in graph[now_n]:
            sum_time[next_n] = max(sum_time[next_n], sum_time[now_n] + build_time[next_n])
            inDegree[next_n] -= 1
            if inDegree[next_n] == 0:
                queue.append(next_n)

for _ in range(t):
    test()