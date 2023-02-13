import sys
input = sys.stdin.readline

N = int(input())
plist = list(map(int, input().split()))
ans_list = []
sum = 0
for i in sorted(plist):
    sum += i
    ans_list.append(sum)
sum = 0
for i in ans_list:
    sum += i
print(sum)

