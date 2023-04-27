n = int(input())
arr = [0 for _ in range(3)]
dp_max = [0 for _ in range(3)]
prev_dp_max = [0 for _ in range(3)]

dp_min = [0 for _ in range(3)]
prev_dp_min = [0 for _ in range(3)]

ans = []

arr = list(map(int, input().split()))
for i in range(3):
    dp_max[i] = arr[i]
    dp_min[i] = arr[i]
    prev_dp_max[i] = arr[i]
    prev_dp_min[i] = arr[i]

for i in range(1,n):
    arr = list(map(int, input().split()))
    dp_max[0] = max(prev_dp_max[0]+arr[0], prev_dp_max[1]+arr[0])
    dp_max[1] = max(prev_dp_max[0]+arr[1], prev_dp_max[1]+arr[1], prev_dp_max[2]+arr[1])
    dp_max[2] = max(prev_dp_max[1]+arr[2], prev_dp_max[2]+arr[2])

    dp_min[0] = min(prev_dp_min[0] + arr[0], prev_dp_min[1] + arr[0])
    dp_min[1] = min(prev_dp_min[0] + arr[1], prev_dp_min[1] + arr[1], prev_dp_min[2] + arr[1])
    dp_min[2] = min(prev_dp_min[1] + arr[2], prev_dp_min[2] + arr[2])

    for i in range(3):
        prev_dp_max[i] = dp_max[i]
        prev_dp_min[i] = dp_min[i]


print(str(sorted(dp_max,reverse=True)[0]) + " " + str(sorted(dp_min)[0]))
