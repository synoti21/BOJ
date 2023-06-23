t = int(input())

def fib(n):
    fib_arr = [[1,0] for _ in range(n+1)]
    if n > 0:
        fib_arr[1][0] = 0
        fib_arr[1][1] = 1

    for i in range(2, n+1):
        fib_arr[i][0] = fib_arr[i-1][0] + fib_arr[i-2][0]
        fib_arr[i][1] = fib_arr[i-1][1] + fib_arr[i-2][1]

    print(fib_arr[n][0], fib_arr[n][1], sep = " ")

for _ in range(t):
    n = int(input())
    fib(n)