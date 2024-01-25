stack = []

for _ in range(int(input())):
    numbers_data = [int(x) for x in input().split()]
    command = numbers_data[0]
    if command == 1:
        stack.append(numbers_data[1])
    elif command == 2:
        if stack:
            stack.pop()
    elif command == 3:
        if stack:
            print(max(stack))
    elif command == 4:
        if stack:
            print(min(stack))

stack.reverse()

print(*stack, sep=', ')
