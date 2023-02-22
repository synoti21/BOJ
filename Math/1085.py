x,y,w,h = map(int, input().split())
print(min(abs(x-w),abs(x),abs(y),abs(y-h)))