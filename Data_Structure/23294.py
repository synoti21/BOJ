# 압축의 경우는 뒷 페이지에서만 일어난다.
# 뒷페이지 공간은 deque을 이용해서 하는 것이 좋아 보인다. 왼쪽, 앞쪽 모두 취급할 수 있으니까.
# 앞페이지 공간은 스택이 좋아보인다. 뒷페이지에 가면 가장 최근에 접속한, 즉 현재 페이지가 가장 맨 위에 있어야 한다.
# 앞으로 갈 경우도 똑같지만, 맨 뒤를 삭제하는 것이 관건이므로 deque. 대신 pop, popleft를 잘 사용해야 겠지
# 중복되는 페이지를 식별해야 하므로 [index, 용량]으로 하는 것이 적절 => dict로 변경
# 압축 시, index를 통해 중복된 것이 있는지 확인한다. 또한, 뒷페이지 공간에서만 일어나므로 queue.remove()를 통해 삭제
# 덱은 indexing을 지원하지 않으므로 모조리 뽑았다가 다시 처음부터 삽입하고, 중복되면 안 넣는걸로

from collections import deque

n,q,c = map(int,input().split())
web_cache = list(map(int,input().split()))
web_dict = {}
comm_list = [[] for _ in range(q)]

back_queue = deque()
front_stack = []

for i in range(len(web_cache)):
    web_dict[i+1] = web_cache[i]

for i in range(q):
    comm = list(map(str,input().split()))
    if comm[0] == 'A':
        comm_list[i] = [comm[0], int(comm[1])]
    else:
        comm_list[i] = [comm[0]]

cur_page = 0
cache = 0
front_cache = 0
back_cache = 0

for i in range(len(comm_list)):
    if comm_list[i][0] == "B" and cur_page and back_queue:
        front_stack.append(cur_page)
        cur_page = back_queue.pop()

    elif comm_list[i][0] == "F" and cur_page and front_stack:
        back_queue.append(cur_page)
        cur_page = front_stack.pop()

    elif comm_list[i][0] == "A":
        for page in front_stack:
            cache -= web_dict[page]

        front_stack.clear()
        if cur_page:
            back_queue.append(cur_page)
        cur_page = comm_list[i][1]
        cache += web_dict[cur_page]

        while cache > c: #조건문 조심
            cache -= web_dict[back_queue.popleft()]
    elif comm_list[i][0] == "C":
        cur = 0
        for i in range(len(back_queue)):
            temp = back_queue.pop()
            if cur != temp:
                back_queue.appendleft(temp)
            else:
                cache -= web_dict[temp]
            cur = temp

print(cur_page)
if len(back_queue) > 0:
    for i in range(len(back_queue)):
        print(back_queue.pop(), end = " ")
    print()
else:
    print(-1)
if len(front_stack) > 0:
    for i in range(len(front_stack)):
        print(front_stack.pop(), end = " ")
    print()
else:
    print(-1)












