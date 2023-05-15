n = int(input())
fac = list(map(int,input().split()))+[0,0]
ans = 0

def buy(case, index):
    global fac, ans

    if case == 3:
        tm = min(fac[index], fac[index+1], fac[index+2])
        fac[index] -= tm
        fac[index+1] -= tm
        fac[index+2] -= tm
        ans += tm*7
    elif case == 2:
        tm = min(fac[index], fac[index+1])
        fac[index] -= tm
        fac[index+1] -= tm
        ans += tm*5
    elif case == 1:
        ans += fac[index]*3


for i in range(n):
    if fac[i+1] > fac[i+2]:
        tm = min(fac[i], fac[i+1]-fac[i+2])
        fac[i] -= tm
        fac[i+1] -= tm
        ans += tm*5
        buy(3,i)
        buy(1,i)

    else:
        buy(3,i)
        buy(2,i)
        buy(1,i)

print(ans)