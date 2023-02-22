t = int(input())
for _ in range(t):
    z_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    a_list = [1 for _ in range(14)]
    k = int(input())
    n = int(input())
    for _ in range(k):
        for i in range(n-1):
            a_list[i+1] = a_list[i]+z_list[i+1]
            z_list[i+1] = a_list[i+1]
    print(a_list[n-1])


