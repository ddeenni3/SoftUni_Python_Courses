def linear_search(input_list, target_element):
    index = -1
    for element_index in range(len(input_list)):
        if input_list[element_index] == target_element:
            index = element_index
            break
    return index


my_list = [1, 3, 5, 7, 9, 11]
target = 7

result = linear_search(my_list, target)

if result != -1:
    print(f"The target element {target} is at index {result}.")
else:
    print(f"The target element {target} was not found in the list.")
