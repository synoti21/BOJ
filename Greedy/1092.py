# -1 : 가장 무거운 박스가 가장 무거운 크레인 보다 무거울 때
# 우선 순위 큐로 먼저 무거운 것 부터 각 크레인에 배정.
# 각 크레인의 상태 배열을 선언
# 우선순위 큐 쓰니까 너무 느리다 그냥 배열 쓰자
# 어차피 상자는 정렬되어 있으니 무거운 것 부터 가벼운 순서대로 각 순회마다 한번씩 다 도는 방향으로

import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int,input().split()))
m = int(input())
box = list(map(int,input().split()))
box.sort(reverse=True)
crane.sort(reverse=True)
crane_status = [0 for _ in range(len(crane))]
box_status = [0 for _ in range(len(box))]
if box[0] > crane[0]:
    print(-1)
    exit()

ans = 0
box_count = len(box)

while box_count > 0:
    c_index = 0
    temp = []
    for i in range(len(box)):
        for j in range(c_index, len(crane)):
            if crane[j] >= box[i] and crane_status[j] == 0:
                temp.append(box[i])
                box_count -= 1
                crane_status[j] = 1
                c_index = j
                break
    ans += 1
    for item in temp:
        box.remove(item)
    crane_status = [0 for _ in range(len(crane))]
print(ans)