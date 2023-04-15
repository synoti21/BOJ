n = int(input())
m = int(input())
target = str(input())

pos = 0
num = 0

def sol(s,st,sl):
    global num,pos,target
    cur_pos = s
    state = st #시작 상태 초기화
    mv = 0
    while True:
        if mv == sl:
            num += 1
            while True: #연쇄적인지 확인
                if cur_pos < m-1 and target[cur_pos] == 'O' and target[cur_pos+1] == 'I':
                    cur_pos += 2
                    num+=1
                else:
                    pos = cur_pos
                    return False
        elif cur_pos == m:
            pos = cur_pos
            return False

        if state == 0 and target[cur_pos] == 'I':
            cur_pos += 1
            state = 1
        elif state == 1 and target[cur_pos] == 'O':
            cur_pos += 1
            state = 0
        else:
            pos = cur_pos
            return False
        mv+=1

while pos < m:
    if target[pos] == 'I':
        sol(pos,0,2*n+1)
    else:
        pos+=1
print(num)