first_string = input()
second_string = input()
third_string = input()

full_list = [first_string, second_string, third_string]

full_list[0], full_list[2] = full_list[2], full_list[0]

print(full_list)
