n= int(input())
fac = list(map(int,input().split()))
ans = 0

def sol(si):
    global ans

    if si < n - 2:
        if fac[si + 1] and fac[si + 2] and fac[si+2] >= fac[si+1]:
            fac[si] -= 1
            fac[si+1] -= 1
            fac[si+2] -= 1
            ans += 7
        elif fac[si+1] and fac[si+1] >= fac[si]:
            fac[si] -= 1
            fac[si+1] -=1
            ans += 5
        else:
            ans += 3
            fac[si] -= 1
    elif si < n-1:
        if fac[si+1] and fac[si+1] >= fac[si]:
            fac[si] -= 1
            fac[si+1] -=1
            ans += 5
        else:
            ans += 3
            fac[si] -= 1
    else:
        ans += 3 * fac[si]
        fac[si] = 0
    return None


for i in range(n):
    if not fac[i]:
        continue
    else:
        while fac[i]:
            sol(i)

print(ans)