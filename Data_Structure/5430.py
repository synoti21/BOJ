import sys
input = sys.stdin.readline

t = int(input())

def sol(s_func, s_arr, s_num):
    rev_status = False

    for exec in s_func:
        if exec == 'R':
            rev_status = (not rev_status)
        elif exec == 'D':

            if s_num > 0:
                if not rev_status:
                    s_arr.pop(0)
                    s_num -= 1
                else:
                    s_arr.pop(-1)
                    s_num -= 1
            else:
                print("error")
                return
    if s_num > 0:
        if rev_status:
            s_arr.reverse()
            print('[',end ='')
            for i in range(s_num-1):
                print(s_arr[i],end =',')
            print(s_arr[-1],end=']\n')

        else:
            print('[', end='')
            for i in range(s_num - 1):
                print(s_arr[i], end=',')
            print(s_arr[-1], end=']\n')
    else:
        print('[]')

for _ in range(t):
    func = list(map(str,input().strip()))
    n = int(input())
    target_str = str(input()).lstrip('[').rstrip(']\n')
    if n > 0:
        arr = list(map(int,target_str.split(',')))
    else:
        arr = []
    for i in range(n):
        arr[i] = int(arr[i])

    sol(func, arr, n)