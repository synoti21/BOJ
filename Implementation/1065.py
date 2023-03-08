n = int(input())
ans = 0
if n < 100:
    print(n)
else:
    ans += 99
    for num in range(100, n+1):
        h = num//100
        t = (num-100*h)//10
        o = num%10
        if h-t == t-o:
            ans+=1
    print(ans)