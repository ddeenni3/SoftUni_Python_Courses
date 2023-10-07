def multiply_result(first, second, third):
    if first == 0 or second == 0 or third == 0:
        return 'zero'
    elif first < 0 or second < 0 or third < 0:
        if first < 0 and second < 0 and third < 0:
            return 'negative'
        elif first < 0 and second < 0:
            return 'positive'
        elif first < 0 and third < 0:
            return 'positive'
        elif second < 0 and third < 0:
            return 'positive'
        return 'negative'
    return 'positive'


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(multiply_result(first_number, second_number, third_number))
