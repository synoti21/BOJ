n, r, c = map(int, input().split())

def sol(size, s_r, s_c, cnt):
    global r, c
    if size == 2:
        print(cnt + (r - s_r) * 2 + (c - s_c))
        return None

    r_size = pow(size,2)//4

    s_size = size // 2
    t_r = s_size + s_r
    t_c = s_size + s_c

    if r >= t_r:
        if c >= t_c:
            sol(s_size, t_r, t_c, cnt + r_size * 3)
        else:
            sol(s_size, t_r, s_c, cnt + r_size * 2)
    else:
        if c >= t_c:
            sol(s_size, s_r, t_c, cnt + r_size)
        else:
            sol(s_size, s_r, s_c, cnt)

sol(pow(2,n),0,0,0)