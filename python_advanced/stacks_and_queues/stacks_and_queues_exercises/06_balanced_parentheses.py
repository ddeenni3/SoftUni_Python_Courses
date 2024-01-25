from collections import deque

parentheses_sequence = deque(input())

opening_parentheses = []

while parentheses_sequence:
    current_parentheses = parentheses_sequence.popleft()
    if current_parentheses in '{[(':
        opening_parentheses.append(current_parentheses)
    elif not opening_parentheses:
        print('NO')
        break
    else:
        if f'{opening_parentheses.pop() + current_parentheses}' not in '{}[]()':
            print('NO')
            break

else:
    print('YES')