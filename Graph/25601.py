n = int(input())
java_class = {}

for i in range(n-1):
    a, b = map(str, input().split())
    java_class[a] = b
fi, se = map(str, input().split())
try:
    parent = java_class[se]
    if parent == fi:
        print(1)
        exit(0)
    while True:
        parent = java_class[parent]
        if parent == fi:
            print(1)
            exit(0)
except KeyError:
    try:
        parent = java_class[fi]
        if parent == se:
            print(1)
            exit(0)
        while True:
            parent = java_class[parent]
            if parent == se:
                print(1)
                exit(0)
    except KeyError:
        print(0)
        exit(0)