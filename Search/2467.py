n = int(input())
arr = list(map(int,input().split()))
start = 0
end = n-1

a_arr = []

while start < end:
    ans = arr[start] + arr[end]
    if ans == 0:
        print(arr[start], arr[end], sep = " ")
        exit()

    if ans > 0:
        a_arr.append((abs(arr[start]+arr[end]),arr[start], arr[end]))
        end -=1
    else:
        a_arr.append((abs(arr[start]+arr[end]),arr[start], arr[end]))
        start +=1

ans_s = sorted(a_arr)[0][1]
ans_f = sorted(a_arr)[0][2]
print(ans_s, ans_f, sep = " ")