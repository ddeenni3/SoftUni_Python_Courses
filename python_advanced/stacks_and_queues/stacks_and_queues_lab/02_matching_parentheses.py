equation = input()

paren_stack = []

for index in range(len(equation)):
    if equation[index] == '(':
        paren_stack.append(index)
    elif equation[index] == ')':
        result = equation[paren_stack.pop():index + 1]
        print(result)
