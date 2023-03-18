#접근법
#어차피 우리는 괄호만 알면 되므로, 다른 문자는 무시하고 괄호만 확인한다.
#두 개의 스택, (스택 과 [스택을 넣고 인식이 될때마다 하나씩 넣는다.
#만약 ), 또는 ]가 나왔을 경우 스택에 (나 [가 있으면 하나를 pop
#비어 있는데 ),]가 나오거나 문자열이 모두 스캔이 완료됐는데 스택이 비어지지 않았으면
#불균형 문자열

import sys
input = sys.stdin.readline

while True:
    stack = []
    flag = 0

    target_str = str(input()).replace("\n","")
    if target_str == '.':
        break
    for i in target_str:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) <= 0:
                flag = 1
                break
            else:
                p = stack.pop()
                if p != '(':
                    flag = 1
                    break
        elif i == ']':
            if len(stack) <= 0:
                flag = 1
                break
            else:
                p = stack.pop()
                if p != '[':
                    flag = 1
                    break
    if len(stack) > 0:
        flag = 1
    if flag == 0:
        print("yes")
    elif flag == 1:
        print("no")