n,b,c = map(int, input().split())
fac = list(map(int,input().split()))+[0,0]
ans = 0
s_cost = b+c
t_cost = b+2*c

if b<=c:
    print(sum(fac)*b)
    exit()

def buy(case, index):
    global fac, ans

    if case == 3:
        tm = min(fac[index], fac[index+1], fac[index+2])
        fac[index] -= tm
        fac[index+1] -= tm
        fac[index+2] -= tm
        ans += tm*t_cost
    elif case == 2:
        tm = min(fac[index], fac[index+1])
        fac[index] -= tm
        fac[index+1] -= tm
        ans += tm*s_cost
    elif case == 1:
        ans += fac[index]*b


for i in range(n):
    if fac[i+1] > fac[i+2]:
        tm = min(fac[i], fac[i+1]-fac[i+2])
        fac[i] -= tm
        fac[i+1] -= tm
        ans += tm*s_cost #로직 다 잘 짜놓고 대체 왜 세 개 사고 있었니...................................................
        buy(3,i)
        buy(1,i)

    else:
        buy(3,i)
        buy(2,i)
        buy(1,i)

print(ans)