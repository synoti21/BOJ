#전깃줄이 교차하는 경우 : 시작 위치, 끝 위치 모두가 크거나 작지 않은 경우. 양 쪽의 대소 관계가 다른 경우 교차
#추가하고자 하는 전깃줄을 추가하느냐와, 추가하지 않느냐 => 갯수 비교, 그럼 전깃줄이 최대로 남게 하면 되는 거겠지?
#구하고자 하는 답은 전깃줄의 최소 개수
#따라서 dp배열도 없애야 하는 전깃줄의 최소 개수를 담아야 할 것

#겹치는 경우 : min(A,B)보다 둘 다 작거나, max(A,B)보다 둘 다 큰 경우 이외의 모든 경우

#dp는 항상 정답만을 가지고 있음 -> 그전까지 전깃줄은 겹치치 않음

#(1,8) -> min (1,8), max (1,8) -> 0
#(3,9) -> min(1,8), max (3,9) -> 0
#(2,2) -> min(1,8)에서 걸림 -> 비교를 해야됨, 왜 (1,8)이 잘렸을까? //(3,9),(2,2)
#(4,1) -> min(2,2)도 걸리고, max(3,9)도 걸림 -> 왜 (4,1)이 잘렸을까?
#(6,4) -> max(3,9)에서 걸림 -> 왜 (3,9)가 잘렸을까?
#(10,10), (9,7), (7,6) 정상

#전깃줄을 추가하려 할 때, 두 개 이상 잘리면 추가하지 않는다.
#아니라면 비교한다. 차이가 더 작은걸 살린다.
#안겹치면 추가한다.

#근데 과거의 것이 겹치면 잘려야된다. => ㅅㅂ
#근데 대소관계가 유지된다는 건 -> 곧 증가한다는 의미 Wow => LIS!!!!
#(1,8) => 0
#(3,9) => 1
#(2,2) => 1
#(4,1) => 0
#(6,4) => 2
#(10,10) =>5
#(9,7) => 4
#(7,6) => 5

n = int(input())
wire = []
arr = [0 for _ in range(n)]
dp = [0 for _ in range(n)]
for i in range(n):
    s,f = map(int, input().split())
    wire.append((s,f))

for i in range(n):
    for j in range(i):
        if wire[j][1] > wire[i][1]:
            temp = wire[j]
            wire[j] = wire[i]
            wire[i] = temp

dp[0] = 1
for i in range(1,n):
    val = 0
    for j in range(i):
        if (wire[i][1] > wire[j][1]) and (wire[i][0] > wire[j][0]) and dp[j] > val:
            val = dp[j]
    dp[i] = val+1

print(n-sorted(dp,reverse=True)[0])

