n = int(input())
arr = [0 for _ in range(n)]
visited = [0 for _ in range(n)]

sum = 0

def isPossible(num, depth):
    if (arr[num] == 1) or abs(depth-num)

def sol(depth):
    if depth == n:
        sum+=1
        return

    for i in range(n):
        if isPossible(i, depth):





