n = int(input())
arr = [0 for _ in range(3)]
dp_max = [0 for _ in range(3)]
dp_min = [0 for _ in range(3)]
ans = []

arr = list(map(int, input().split()))
for i in range(3):
    dp_max[i] = arr[i]
    dp_min[i] = arr[i]

for i in range(1,n):
    arr = list(map(int, input().split()))
    dp_max[0] = dp_max[0] + max(arr[0], arr[1])
    dp_max[1] = dp_max[1] + max(arr[0], arr[1], arr[2])
    dp_max[2] = dp_max[2] + max(arr[1], arr[2])

    dp_min[0] = dp_min[0] + min(arr[0], arr[1])
    dp_min[1] = dp_min[1] + min(arr[0], arr[1], arr[2])
    dp_min[2] = dp_min[2] + min(arr[1], arr[2])
    print(dp_max)
    print(dp_min)

print(str(sorted(dp_max,reverse=True)[0]) + " " + str(sorted(dp_min)[0]))
