first_string = input()
second_string = input()

last_printed_string = first_string

for ch in range(0, len(first_string)):

    string_one = second_string[:ch + 1]
    string_two = first_string[ch + 1:]
    current_string = string_one + string_two
    if current_string != last_printed_string:
        print(current_string)
        last_printed_string = current_string
    else:
        continue
