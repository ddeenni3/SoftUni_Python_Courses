def string_in_string(first: list, second: list) -> list:
    result = []
    for word in first:
        for current_word_second in second:
            if word in current_word_second and word not in result:
                result.append(word)
                continue
    return result


first_string = input().split(', ')
second_string = input().split(', ')

print(string_in_string(first_string, second_string))
