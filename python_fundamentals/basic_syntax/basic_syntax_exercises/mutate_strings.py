first_string = input()
second_string = input()

last_printed_string = first_string

for char in range(len(first_string)):
    left_side = second_string[:char + 1]  # [0:char + 1 : 1]
    right_side = first_string[char + 1:]  # [char + 1 : len(first_string) : 1]

    current_string = left_side + right_side
    if last_printed_string == current_string:
        continue
    else:
        last_printed_string = current_string
        print(current_string)
