chem = list(map(str,input().strip()))
ch_dic = {'H': 1, 'C': 12, 'O': 16}
stack =[]
temp = 0

for i in range(len(chem)):
    if chem[i] == '(':
        stack.append(chem[i])
    elif chem[i] == ')':
        while len(stack) > 0 and stack[-1] != '(':
            temp += stack[-1]
            stack.pop()
        stack.pop()
        stack.append(temp)
        temp = 0
    elif chem[i].isdigit():
        chem_top = stack.pop()
        stack.append(chem_top*int(chem[i]))
    else:
        stack.append(ch_dic[chem[i]])
print(sum(stack))