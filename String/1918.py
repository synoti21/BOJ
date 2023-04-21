target = list(map(str,input().strip()))
opr_stack = []
ans = []


for char in target:

    if char.isalpha():
        ans.append(char)
    elif char == '(':
        opr_stack.append('(')
    elif char == ')':
        cur = opr_stack[len(opr_stack)-1]
        while cur != '(':
            ans.append(opr_stack.pop())
            cur = opr_stack[len(opr_stack) - 1]
        opr_stack.pop()
    else:
        if len(opr_stack) > 0:
            front = opr_stack[len(opr_stack) - 1]
        else:
            front = '$'

        if (char == '*' or char == '/'):
            if front == '*' or front == '/':
                ans.append(opr_stack.pop())
            opr_stack.append(char)
        else:
            if front == '*' or front == '/':
                front_temp = opr_stack[len(opr_stack) - 1]
                while front_temp != '(':
                    opr = opr_stack.pop()
                    ans.append(opr)
                    if len(opr_stack) > 0:
                        front_temp = opr_stack[len(opr_stack) - 1]
                    else:
                        front_temp = '('
                opr_stack.append(char)
            elif front == '+' or front == '-':
                ans.append(opr_stack.pop())
                opr_stack.append(char)
            else:
                opr_stack.append(char)

while len(opr_stack) != 0:
    ans.append(opr_stack.pop())

for i in ans:
    print(i,end= '')