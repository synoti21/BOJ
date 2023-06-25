#promising function을 이용 (heurastic value)
#minimization optimization의 문제이므로, h value는 underestimated value
#incoming edge와 outgoing edge가 있으므로, n번째 행의 최소값과 n번째 열의 최소값의 평균
#즉, 나가는 간선과 오는 간선의 평균을 구하기
#이건 Branch & Bound Approach

import sys

input = sys.stdin.readline
n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]
# 최종적으로 도시를 모두 방문했는지 확인하기 위한 상수 (1111110, 0은 시작도시 1)
VISITED_ALL = (1 << n) - 1

# 각 도시 * 해당 도시를 마지막으로 방문했을 때, 지금까지 방문한 도시 (DP이므로, 문제를 쪼갠다. 첫번째 index는 문제의 범위. 두번째 인덱스는 지금까지 방문한 도시들,
# ex cache[2][6] = 8 => 현재 n = 2고 지금까지 방문한 도시는 0110, 즉 2번 3번 도시만 방문했다는 뜻, 그리고 이 때 최단 경로는 8)
cache = [[None] * (1 << n) for _ in range(n)]
INF = float('inf')
idx = 1

def find_path(last, visited):
    if visited == VISITED_ALL:
        # 모두 방문했을 때, 마지막 도시와 출발도시가 연결되어 있으면 return, 연결 안되어 있으면 (0) INF 반환

        return cities[last][0] or INF  # 마지막 도착 도시에서 출발 도시인 0으로 가야됨.(문제 조건)

    # 현재 마지막으로 방문한 도시가 last고 현재까지 방문했던 도시들의 경로가 갱신이 되어있다면 넘어감
    if cache[last][visited] is not None:
        return cache[last][visited]

    tmp = INF
    for city in range(n):
        # 아직 city를 방문하지 않앗고, 해당 도시와 마지막 방문한 도시가 연결되어 있으면 재귀문 호출
        if visited & (1<< city) == 0 and cities[last][city] != 0:
            tmp = min(tmp, find_path(city, visited | (1 << city)) + cities[last][city]) #마지막 도시와 연결되어 있는 아직
            #방문하지 않은 도시들 중, 더 짧은 도시들을 선택한다.
    cache[last][visited] = tmp
    return tmp

print(find_path(0, 1 << 0))
