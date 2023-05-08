l,c = map(int,input().split())
arr = list(map(str,input().split()))
arr.sort()
vow= ['a','e','i','o','u']
visited = [0 for _ in range(c)]
ans = []

vow_cnt = 0
con_cnt = 0

for char in arr:
    if char in vow:
        vow_cnt +=1
if not (vow_cnt > 0 and len(arr)-vow_cnt > 1):
    exit()

def sol(depth, s_vow, s_con, index):
    global ans

    if depth == l:
        if s_vow > 0 and s_con > 1:
            print(*ans, sep="")

    for i in range(c):
        if visited[i] == 0 and i > index:
            visited[i] = 1
            ans.append(arr[i])
            if arr[i] in vow:
                sol(depth+1, s_vow+1, s_con, i)
            else:
                sol(depth+1,s_vow,s_con+1, i)
            ans.pop()
            visited[i] = 0

sol(0,0,0,-1)