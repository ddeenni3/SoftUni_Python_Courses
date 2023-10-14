number_of_electrons = int(input())

result = []
n = 1
while number_of_electrons > 0:
    current_shell_space = 2 * n ** 2
    if number_of_electrons - current_shell_space > 0:
        result.append(current_shell_space)
        number_of_electrons -= current_shell_space
    else:
        current_shell_space = number_of_electrons
        result.append(current_shell_space)
        number_of_electrons -= current_shell_space
    n += 1

print(result)
