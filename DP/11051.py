t = int(input())


def sol():
    n = int(input())
    arr = list(map(int,input().split()))

    max = arr[len(arr)-1]
    sum = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max:
            max = arr[i]
        else:
            sum += max - arr[i]
    print(sum)

for _ in range(t):
    sol()