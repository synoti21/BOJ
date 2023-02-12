from math import *


def solution(n, k):
    ans = 0
    dividend = n
    divisor = k

    res_str = ""

    while dividend > 0:
        res_str += str(dividend % divisor)
        dividend = dividend // divisor

    res_str = res_str[::-1]
    res_str = res_str.split("0")
    res_str = ' '.join(res_str).split()

    for i in range(0, len(res_str)):
        if (int(res_str[i]) >= 2):
            flag = True
            for j in range(2, floor(sqrt(int(res_str[i]))) + 1):
                if (int(res_str[i]) % j == 0):
                    flag = False
                    break
            if flag == True:
                ans += 1

    return ans
